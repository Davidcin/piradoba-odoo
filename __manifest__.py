# -*- coding: utf-8 -*-
{
    'name' : 'Piradoba',
    'version' : '1.0',
    'summary': 'List of identities',
    'sequence': -200,
    'description': "List of identities and information about them.",
    'category': 'Productivity',
    'website': 'https://github.com/Davidcin',
    'images' : ['icon.png'],
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/piradoba.xml',
        'report/report_pdf_template.xml',
        'report/report.xml'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
