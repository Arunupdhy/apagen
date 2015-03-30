import time
import datetime

from openerp.osv import fields, osv
from openerp.tools.translate import _

class stock_picking(osv.osv):
    _inherit = "stock.picking"
    
    _columns = {
    	'transfer_by': fields. many2one('res.users', 'Transferred By', readonly=1),
    	'transfer_date': fields.datetime('Transfer Date'),
    	}
    _defaults = {
        'transfer_date': fields.date.context_today,
        'transfer_by': lambda obj, cursor, user, context: user,
    }
    
class stock_inventory(osv.osv):
    _inherit = "stock.inventory"
    
    _columns = {
    	'responsible': fields.many2one('res.users', 'Responsible', required=1),
    	}
    
    
