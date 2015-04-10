# Copyright 2014-2015 - Apagen Solutions Pvt. Ltd.
{
    'name': 'Warehouse_Media',
        'version': '1.0',
        'category': 'Media Industry',
        'sequence': 14,
        'summary': 'Media Industry',
#        'description': """
 #       """,
        'author': 'Apagen Solution Pvt Ltd.',
        'website': 'http://www.apagen.com',
        'depends': ['stock'
    ],
    'init_xml': [
    ],
    'data': [
        'wizard/stock_move_history_view.xml',
        'report/report.xml',        
    	'views/report_stockmove.xml',
    	'views/report_stockpicking.xml',
    	'views/report_stockinventory.xml',
        'views/report_stockvaluation.xml',    	
        'warehouse_media_view.xml',
    	'stock_report.xml',
        
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
