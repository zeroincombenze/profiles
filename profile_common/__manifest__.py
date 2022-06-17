# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# Copyright 2022 LibrERP enterprise network <https://www.librerp.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
{
    'name': 'profile common',
    'summary': 'Common setup for all profiles',
    'version': '12.0.0.1.1',
    'category': 'Technical Settings',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'depends': [
        'account',
        'account_cancel',
        'purchase',
        'sale',
        'sale_management',                                      # Only 12.0
        'stock',
    ],
    'data': ['data/initial_conf.xml'],
    'installable': True,
    'maintainer': 'Antonio Maria Vigliotti',
    'development_status': 'Beta',
}
