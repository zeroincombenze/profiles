# -*- coding: utf-8 -*-
#
# Copyright 2019-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    'name': 'profile zeroincombenze(R)',
    'version': '10.0.0.1.1',
    'category': 'Technical Settings',
    'summary': 'Zeroincombenze',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'depends': [
        'profile_common',
        'account_invoice_check_total',
        'account_payment_term_extension',
        'disable_odoo_online',
        'l10n_it_einvoice_in',
        'l10n_it_einvoice_out',
        'l10n_it_fiscal',
        'l10n_it_ricevute_bancarie',
        'purchase',
        'purchase_discount',
        'remove_odoo_enterprise',
    ],
    'data': ['data/initial_conf.xml'],
    'installable': True,
    'maintainer': 'Antonio Maria Vigliotti',
    'development_status': 'Beta',
}
