# -*- coding: utf-8 -*-
#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "profile_base",
    "version": "10.0.1.0.2",
    "category": "Technical Settings",
    "summary": "Base profile",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "base",
        "l10n_it_fiscal",
        "partner_bank",
        # "partner_data_from_vies",
        "purchase",
        "purchase_discount",
        "report_xlsx",
        "sale",
        # 'sale_management',                    # Only 12.0
        "stock",
        "web_responsive",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
