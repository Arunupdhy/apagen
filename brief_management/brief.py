from openerp.osv import osv, fields
from datetime import date

class brief(osv.osv):
    _name = "brief"
    _inherit = ['mail.thread', 'ir.needaction_mixin']

    def _get_default_section_id(self, cr, uid, context=None):
        """ Gives default section by checking if present in the context """
        return self._resolve_section_id_from_context(cr, uid, context=context) or False

    def _resolve_section_id_from_context(self, cr, uid, context=None):
        """ Returns ID of section based on the value of 'section_id'
            context key, or None if it cannot be resolved to a single
            Sales Team.
        """
        if context is None:
            context = {}
        if type(context.get('default_section_id')) in (int, long):
            return context.get('default_section_id')
        if isinstance(context.get('default_section_id'), basestring):
            section_name = context['default_section_id']
            section_ids = self.pool.get('crm.case.section').name_search(cr, uid, name=section_name, context=context)
            if len(section_ids) == 1:
                return int(section_ids[0][0])
        return None

    STATE_SELECTION = [
        ('draft', 'Draft'),
        ('awaiting_approval', 'Awaiting Approval'),
        ('approved', 'Approved'),
        ('cancel', 'Cancelled'),
        ('pending', 'Pending'),
    ]

    _track = {

        'state': {
            'brief_management.brief_awaiting_approval': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'awaiting_approval',
            'brief_management.brief_approved': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'approved',
            'brief_management.brief_cancel': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'cancel',
            'brief_management.brief_pending': lambda self, cr, uid, obj, ctx=None: obj['state'] == 'pending',

        },
    }

    _columns = {
        'partner_id': fields.many2one('res.partner', 'Customer'),
        'advertiser_id': fields.many2one('res.partner', 'Advertiser'),
        'advertiser_category': fields.many2one('brief.category', 'Category'),
        'brief_no':fields.char('Brief No.'),
        'brief_date':fields.date('Brief Date'),
        'user_id': fields.many2one('res.users', 'Assigned To'),
        'section_id': fields.many2one('crm.case.section', 'Sales Team', help='When sending mails, the default email address is taken from the sales team.'),   
        'brand_id': fields.many2one('brand', 'Brand'),
        'state': fields.selection(STATE_SELECTION,
            'Status', readonly=True, select=True),
        'notes': fields.text('Notes', states={'draft': [('readonly', False)]}),     
        'brief_type': fields.selection([
            ('promotion', 'Promotion'),
            ('classified', 'Classified'),
            ('spot_ads', 'Spot Ads'),
            ], 'Brief Type'),   
        'start_date':fields.date('Expected Start Date'),
        'end_date':fields.date('Expected End Date'), 
        'due_date': fields.date('Due Date'),
        'create_by': fields.many2one('res.users','Created By'),
        'product': fields.many2one('product.product','Product'),
                   
    }
    
    _defaults = {
        'user_id': lambda obj, cr, uid, context: uid,
        'create_by': lambda obj, cr, uid, context: uid,
        'brief_date': fields.date.context_today,
        'section_id': lambda s, cr, uid, c: s._get_default_section_id(cr, uid, c),
        'state': 'draft'
    }

    def on_change_user(self, cr, uid, ids, user_id, context=None):
        """ When changing the user, also set a section_id or restrict section id
            to the ones user_id is member of. """
        if user_id:
            section_ids = self.pool.get('crm.case.section').search(cr, uid, ['|', ('user_id', '=', user_id), ('member_ids', '=', user_id)], context=context)
            if section_ids:
                return {'value': {'section_id': section_ids[0]}}
        return {'value': {}}

    def submit_request(self, cr, uid, ids, context=None):
        seq = self.pool.get('ir.sequence').get(cr, uid, 'brief') or '/'
        self.write(cr, uid, ids, {'state': 'awaiting_approval', 'brief_no': seq})
        return True

    def approve_request(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'approved'})
        return True

    def cancel_request(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'cancel'})
        return True

    def pending_request(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state': 'pending'})
        return True

    def reset_draft(self, cr, uid, ids, context=None):
        self.write(cr, uid, ids, {'state':'draft'}, context=context)
        return True    

class brand(osv.osv):
    _name = 'brand'
    _columns = {
        'name': fields.char("Name", required='True'),
        'type': fields.selection([('1', "Radio"), ('2', 'TV'), ('3', 'Digital')],
                                 "Type", required='True'),
        'company_id': fields.many2one('res.company', 'Company', required=True, select=1),
        
    }        

class brief_category(osv.osv):
    _name = 'brief.category'
    _columns = {
        'name': fields.char("Name")
        }
        
