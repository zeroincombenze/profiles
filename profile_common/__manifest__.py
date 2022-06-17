# -*- coding: utf-8 -*-
#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
{
    "name": "profile common",
    "version": "10.0.0.1.2",
    "category": "Technical Settings",
    "summary": "Common setup for all profiles",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "LGPL-3",
    "depends": [
        "account",
        "account_cancel",
        "purchase",
        "sale",
        # 'sale_management',                    # Only 12.0
        "stock",
    ],
    "data": ["data/initial_conf.xml"],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
}
