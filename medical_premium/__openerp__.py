# coding: utf-8
# Copyright 2014-2015 - Apagen Solutions Pvt. Ltd.
{
    'name': 'Medical Premium',
    'version': '1.0',
    'category': 'Human Resources',
    #'sequence': 19,
    'summary': 'Medical Premium',
    'description': """

    """,
    "author": "Apagen Solutions Pvt. Ltd.",
    'website': 'http://www.apagen.com',
    'depends': [
        'hr'
        ],
    'data': [
        'medical_premium_view.xml',
        'medical_premium_sequence.xml',
        'medical_premium_workflow.xml',
    ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: