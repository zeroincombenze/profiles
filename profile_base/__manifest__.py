#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Base profile",
    "version": "12.0.1.0.3",
    "category": "Technical Settings",
    "summary": "Base setup for minimal configuration",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "base",
        "remove_odoo_enterprise",           # OCA server-brand - Only 12.0
        "disable_odoo_online",              # OCA server-brand - Only 12.0
        # "l10n_it_coa",
        "portal_odoo_debranding",           # OCA server-brand - Only 12.0
        # "partner_data_from_vies",
        "purchase",
        "purchase_discount",
        "report_xlsx",
        "repository_check",                  # custom-addons - Only 12.0
        "sale",
        'sale_management',  # Only 12.0
        "stock",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
