# -*- coding: utf-8 -*-
{
    'name': "Library Management",

    'summary': """
        Library Management""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ana Hernandez",
    'website': "https://github.com/ianahernandez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/data.xml',
        'security/groups.xml',
        'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/library_book_view.xml',
        'views/library_book_category_view.xml'
    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode

}