# -*- coding: utf-8 -*-
{
    'name': "Sales Tolerance",
    'version': '1.0',
    'depends': ['base', 'contacts', 'sale', 'sale_stock'],
    'sequence': 1,
    'author': "Suni",
    'category': 'All',
    'description': """
    Property Management
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',

        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/stock_picking_view.xml',
        'views/sale_tolerance_menu_view.xml',
        
        'wizard/sale_order_confirmation_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

