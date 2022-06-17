# Copyright 2019-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# Copyright 2022 LibrERP enterprise network <https://www.librerp.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
{
    "name": "profile zeroincombenze(R)",
    "version": "10.0.0.1.1",
    "category": "Technical Settings",
    "summary": "Zeroincombenze",
    "author": "SHS-AV s.r.l.",
    "website": "https://github.com/OCA/l10n-italy",
    "depends": [
        "profile_common",
        "account_invoice_check_total",
        "account_payment_term_extension",
        "disable_odoo_online",
        "l10n_it_einvoice_in",
        "l10n_it_einvoice_out",
        "l10n_it_fiscal",
        "l10n_it_ricevute_bancarie",
        "purchase",
        "purchase_discount",
        "remove_odoo_enterprise",
    ],
    "data": ["data/initial_conf.xml"],
    "installable": True,
    "maintainer": "Antonio Maria Vigliotti",
    "development_status": "Beta",
}
