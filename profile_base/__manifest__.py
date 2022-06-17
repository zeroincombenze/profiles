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
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "base",
        "remove_odoo_enterprise",           # OCA server-brand - Only 12.0
        "disable_odoo_online",              # OCA server-brand - Only 12.0
        "portal_odoo_debranding",           # OCA server-brand - Only 12.0
        # "partner_data_from_vies",
        "l10n_it_fiscalcode",
        "report_xlsx",
        "repository_check",                  # custom-addons - Only 12.0
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
