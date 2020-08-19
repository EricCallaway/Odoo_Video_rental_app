# -*- coding: utf-8 -*-
{
    'name': "Movie_Rentals",

    'summary': """
        Software that is specifically designed for movie rental companies. 
        This Video rental store now also rents out video games!!
        """,

    'description': """
        This program will help keep track of inventory, customer data, sales/ accounting, and so much more!
    """,

    'author': "Eric Callaway",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
         'security/ir.model.access.csv', #This is the modified security access file
         #'views/views.xml',
         'views/movies.xml',
         'views/video_games.xml',
         #'views/orders.xml', #This view is not working at the moment

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}