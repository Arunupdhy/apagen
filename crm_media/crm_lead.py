from openerp.osv import osv, fields

class crm_lead(osv.osv):
    _inherit = "crm.lead"

    _columns = {
        'channel_id': fields.many2one('crm.tracking.medium', 'Lead Source', help="Communication channel (mail, direct, phone, ...)"),
        'brand_id': fields.many2one('brand', 'Brand', required='True'),
        }
        
    def action_schedule_meeting(self, cr, uid, ids, context=None):
        """
        Open meeting's calendar view to schedule meeting on current opportunity.
        :return dict: dictionary value for created Meeting view
        """
        lead = self.browse(cr, uid, ids[0], context)
        res = self.pool.get('ir.actions.act_window').for_xml_id(cr, uid, 'calendar', 'action_calendar_event', context)
        partner_ids = [self.pool['res.users'].browse(cr, uid, uid, context=context).partner_id.id]
        if lead.partner_id:
            partner_ids.append(lead.partner_id.id)
        res['context'] = {
            'default_opportunity_id': lead.type == 'opportunity' and lead.id or False,
            'default_partner_id': lead.partner_id and lead.partner_id.id or False,
            'default_partner_ids': partner_ids,
            'default_section_id': lead.section_id and lead.section_id.id or False,
            'default_name': lead.name,
        }
        return res
        
    def action_quotation_send(self, cr, uid, ids, context=None):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        ir_model_data = self.pool.get('ir.model.data')
        try:
            template_id = ir_model_data.get_object_reference(cr, uid, 'sale', 'email_template_edi_sale')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference(cr, uid, 'mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False 
        ctx = dict()
        ctx.update({
            'default_model': 'sale.order',
            'default_res_id': ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
            'default_composition_mode': 'comment',
            'mark_so_as_sent': True
        })
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form_id, 'form')],
            'view_id': compose_form_id,
            'target': 'new',
            'context': ctx,
        }

class brand(osv.osv):
	_name = 'brand'
	_columns = {
		'name': fields.char("Name", required='True'),
		'type': fields.selection([('1', "Radio"), ('2', 'TV'), ('3', 'Digital')],
		                         "Type", required='True'),
		'company_id': fields.many2one('res.company', 'Company', required=True, select=1),
		
	}
	
class calendar_event(osv.Model):
    """ Model for Calendar Event """
    _inherit = 'calendar.event'
    _columns = {
    	'status1': fields.selection([
            ('scheduled','Scheduled'),
            ('progress','In Progress'),
            ('complete','Complete'),
            ], 'state'),
     	'status': fields.selection([('scheduled', "Scheduled"), ('progress', 'In Progress'), ('complete', 'Complete')],
		                         "Status", required='True'),
		        }
		        
    def onchange_status(self, cr, uid, ids, status, context=None):
		if status:
			return {'value' : {'status1': status}}
