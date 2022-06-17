# Copyright 2022 LibrERP enterprise network <https://www.librerp.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#

{
    'name': 'Profilo di base',
    'summary': "Profilo di base per tutte le installazioni",
    'version': '12.0.1.0.1',
    'category': 'Localization/Account Charts',
    'depends': [
        'base',
        'remove_odoo_enterprise',  # OCA server-brand
        'disable_odoo_online',
        'partner_data_from_vies',
        'l10n_it_fiscalcode',    # OCA l10n_italy
        'report_xlsx',  # OCA reporting-engine
        'repository_check'
    ],
    'author': """
        Powerp
    """,
    'website': 'http://www.powerp.it/',
    'license': 'AGPL-3',
    'data': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False
}
