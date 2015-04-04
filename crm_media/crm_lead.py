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

class brand(osv.osv):
	_name = 'brand'
	_columns = {
		'name': fields.char("Name", required='True'),
		'type': fields.selection([('1', "Radio"), ('2', 'TV'), ('3', 'Digital')],
		                         "Type", required='True'),
		'company_id': fields.many2one('res.company', 'Company', required=True, select=1),
		
	}
