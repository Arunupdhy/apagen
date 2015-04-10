from openerp.osv import osv, fields
from datetime import date

class children(osv.osv):
    _name = 'employee.children'
    _columns = {
        'surname':fields.char('Surname', size=32),
        'name':fields.char('First & Middle Name', size=32),
        'date_of_birth':fields.date('Date of Birth'),
        'age':fields.integer('Age'),
        'relationship':  fields.selection([('son', "Son"),
                                           ('daughter', "Daughter")],
                                          "Relationship"),
        'studying':  fields.selection([('yes', "Yes"),
                                       ('no', "No")],
                                      "Studying in College?"),
        'college_year':  fields.selection([('one', "1"),
                                           ('two', "2"),
                                           ('three', "3"),
                                           ('four', "4"),
                                           ('five', "5"),
                                           ('six', "6")],
                                          "College Year"),
        'children_id': fields.many2one('hr.employee', 'Children Id'),
    }

class hr_employee(osv.osv):
    _inherit = 'hr.employee'
    _columns = {
        'children_ids':fields.one2many('employee.children', 'children_id', 'Children'),
    }
