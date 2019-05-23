# -*- coding: utf-8 -*-
{
    'name': "Product price update wizard",

    'summary': """
        Product price update wizard""",

    'description': """
        Asistente para la actualizacion de precio de los productos de forma masiva, de acuerdo a la variación de la tasa del dólar
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
        'wizard/product_price_update_wizard_view.xml',

    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode

}