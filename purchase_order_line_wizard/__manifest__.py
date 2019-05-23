# -*- coding: utf-8 -*-
{
    'name': "Purchase order line wizard",

    'summary': """
        Purchase order line wizard""",

    'description': """
        Purchase order line wizard
    """,

    'author': "Ana Hernandez",
    'website': "https://github.com/ianahernandez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'wizard/purchase_order_line_wizard_view.xml',

    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode

}