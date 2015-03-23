# -*- coding: utf-8 -*-

{
    'name': 'Purchase_Media',
    'version': '1.0',
    'author': 'Apagen Solutions Pvt. Ltd.',
    'category': 'Purchases',
    'sequence': 1,
    'website': 'http://www.apagen.com',
    'summary': '',
    'description': """This application extends functionality of Purchases for Radio Africa Group""",
    'depends': ['purchase', 'purchase_requisition'],
    'data': [
        'purchase_view.xml',
        'purchase_report.xml',
        #'purchase_requisition_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
