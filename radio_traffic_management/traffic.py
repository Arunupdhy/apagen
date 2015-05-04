from openerp.osv import osv, fields
from datetime import datetime, timedelta
import datetime
from datetime import date

class daily_traffic(osv.osv):
    _name = "daily.traffic"
    #_rec_name = 'std_id'

    _columns = {
    'state': fields.selection([
            ('draft','Draft'),
            ('scheduled','Scheduled'),
            ('executed','Executed'),
            ('cancelled','Cancelled'),
            ], 'Status', readonly=True),
    'ref': fields.char('Reference'),
    'brand': fields.many2one('brand','Brand',required=1),
    'create_date': fields.datetime('Creation Date',readonly=1),
    'traffic_date': fields.date('Traffic Date',required=1),
    'responsible': fields.many2one('res.users','Responsible',required=1),
    'traffic_line': fields.one2many('daily.traffic.lines', 'traffic_id', 'Traffic Lines'),
    }
    _defaults = {
    	'create_date': fields.date.context_today,
    	'traffic_date': fields.date.context_today,
        'state': 'draft',
    	'responsible': lambda obj, cr, uid, context: uid,
    	#self.write(cr, uid, ids,{'ref': self.pool.get('ir.sequence').get(cr, uid, 'daily.traffic')or '/'},context=context)
    }
    	
class daily_traffic_lines(osv.osv):
    _name = "daily.traffic.lines"

    _columns = {
    'traffic_id': fields.many2one('daily.traffic','Line ID'),
    'status': fields.selection([
            ('draft','Draft'),
            ('scheduled','Scheduled'),
            ('executed','Executed'),
            ('notexe','Not Executed'),
            ], 'Status'),
    'spot_id': fields.char('Spot ID',required=1),
    'time_start': fields.datetime('Time Start',required=1),
    'time_end': fields.datetime('Time End',required=1),
    'product': fields.many2one('product.product','Product',required=1),
    'description': fields.char('Description',required=1),
    'advertiser': fields.many2one('res.partner','Advertiser',required=1),
    'remark': fields.char('Remarks'),
    }
    

