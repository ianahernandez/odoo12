# -*- coding: utf-8 -*-
{
    'name': "Product Template (Herencia)",

    'summary': """
        Product Template (Herencia)""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ana Hernandez",
    'website': "https://github.com/ianahernandez",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml',

    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode

}