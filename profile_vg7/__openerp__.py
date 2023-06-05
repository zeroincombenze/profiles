# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'profile VG7',
    'summary': '''VG7 customer profile''',

    'description': '''
VG7 customer profile
--------------------

This module manage VG customer profile.
    ''',

    'author': 'SHS-AV s.r.l.',
    'website': 'http://www.shs-av.com',
    'category': 'Technical Settings',
    'version': '8.0.0.1.0',
    # any module necessary for this one to work correctly
    'depends': ['purchase'],
    'data': [
        'data/initial_conf.xml',
        'views/purchase_order_view.xml',
    ],
    'active': False,
    'installable': True
}
