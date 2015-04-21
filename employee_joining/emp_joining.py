from openerp.osv import fields, osv
from openerp import netsvc
from openerp import pooler
from openerp.tools.translate import _
from datetime import datetime,date
from json import dumps
import time
import datetime

class Joining(osv.osv):
	_name = 'joining'
	_description = 'Employee Joining'
	_inherit = 'mail.thread'
    
    
    
	_columns = {
		'state': fields.selection([('in_progress',"In Progress"),
        									  ('w_c_a', "Waiting COO Approval"),('induction', "Induction"),('closed',"Closed")],"Status"),
		'employee_id':fields.many2one('hr.employee','Employee',required=True),
		'job_Position':fields.many2one('hr.job','Job Position',required=True),
		'department_id':fields.many2one('hr.department','Department',required=True),
		'joining_date':fields.datetime('Joining Date',required=True, readonly=True),
		'required_items':fields.one2many('req.items','req_id','Required Items'),
		'confirm_receipt':fields.boolean('Confirmation Receipt'),
		's_w_email':fields.boolean('Send Welcome Email'),
		'i_to_staff':fields.boolean('Introduction to Staff'),
		's_id_card':fields.boolean('Submit ID Card Form'),
		's_m_form':fields.boolean('Submit Medical Form'),
		'induction':fields.one2many('induction','ind_id','Induction'),
		'emp_joining_ref':fields.char('Employee Joining Reference'),
	}
	_defaults = {
		'joining_date': datetime.datetime.now(),
        #'state': 'in_progress',
	    }
	def draf(self,cr,uid,ids,context=None):
		print"--------------one"
		self.write(cr, uid,ids,{'state':'draft'},context=context)
		return True
		
	def state_in_progress(self, cr, uid, ids, context=None):
		print"--------------two"
		#self.write(cr,uid, ids, {'state':'in_progress'}, context=context)
		self.write(cr, uid, ids, {'emp_joining_ref':self.pool.get('ir.sequence').get(cr, uid, 'joining') or '/'},context=context)
		return True
	
	def state_coo_aproval(self,cr,uid, ids, context=None):
		print"--------------three"
		self.write(cr,uid, ids, {'state':'w_c_a'}, context=context)
		return True
	
	def state_induction(self, cr, uid, ids, context=None):
		print"--------------four"
		self.write(cr, uid, ids, {'state': 'induction'}, context=context)
		return True

	def state_reset(self, cr, uid, ids, context=None):
		print"--------------five"
		self.write(cr, uid, ids, {'state': 'in_progress'}, context=context)

	def state_close(self, cr, uid, ids, context=None):
		print"--------------six"
		self.write(cr, uid, ids, {'state': 'closed'}, context=context)
		return True
		
			 	 

    
class Required_Items(osv.osv):
	_name = 'req.items'
	_rec_name='item_name'
	
	_columns = {
	
		'req_id': fields.many2one('joining',"Required Item"),
		'item_name'	: fields.char('Item Name', required=True),
		'quantity': fields.float('Quantity', required=True),
		'department_id':fields.many2one('hr.department','Department',required=True),
		'remarks': fields.char("Remarks", required=True),
		'status': fields.selection([('in_progress',"In Progress"),
        									  ('received', "Received")],"Status",required=True),
		'status1': fields.selection([('in_progress',"In Progress"),
        									  ('received', "Received")],"Status"),
		}

	def onchange_status(self, cr, uid, ids, status, context=None): 
		if status:
			return {'value' : {'status1':status}}
	
class Induction(osv.osv):
	_name = 'induction'
	_rec_name='company_id'
	
	_columns = {
	
		'ind_id': fields.many2one('joining','Induction'),
		'company_id': fields.char('Company', required=True),
		'responsible':fields.many2one('hr.employee','Responsible',required=True),
		'remarks_id': fields.char("Remarks", required=True),
		}		
