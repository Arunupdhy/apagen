from datetime import datetime, timedelta
import time
import datetime
from openerp.osv import fields, osv


class purchase_requisition(osv.osv):
	_inherit = "purchase.requisition"
	_description = "Purchase Requisition"
 

	_columns = {
		'creation_date': fields.datetime('Creation Date',required=True),
		#'exclusive': fields.selection([('exclusive', 'Select only one RFQ (exclusive)'), ('multiple', 'Select multiple RFQ')], 'Requisition Type', required=True, help="Select only one RFQ (exclusive):  On the confirmation of a purchase order, it cancels the remaining purchase order.\nSelect multiple RFQ:  It allows to have multiple purchase orders.On confirmation of a purchase order it does not cancel the remaining orders"""),
		#'origin': fields.char('source document'),
		#'ordering_date' : fields.datetime('Requsition Date'),
		#'date_end': fields.datetime('Requsition Deadline'),
		#'company_id': fields.many2one('res.company', 'Company', required=True),
		
	}
	_defaults = {
		'creation_date': datetime.datetime.now(),
	}

	
	

