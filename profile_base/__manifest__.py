# Copyright 2022 LibrERP enterprise network <https://www.librerp.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
{
    "name": "Profilo di base",
    "version": "12.0.1.0.1",
    "category": "Localization/Account Charts",
    "summary": "Profilo di base per tutte le installazioni",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        "base",
        "remove_odoo_enterprise",
        "disable_odoo_online",
        "partner_data_from_vies",
        "l10n_it_fiscalcode",
        "report_xlsx",
        "repository_check",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
