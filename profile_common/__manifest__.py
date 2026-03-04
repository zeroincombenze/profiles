# -*- coding: utf-8 -*-
#
# Copyright 2016-26 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "Common profile",
    "version": "10.0.1.0.5",
    "category": "Technical Settings",
    "summary": "Common setup for all profiles",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it/crm",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "calendar",
        "contacts",
        "mail",
        "product",
        "stock",
        "web_decimal_numpad_dot",
    ],
    "data": ["data/initial_conf.xml"],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    "post_init_hook": "set_default_values",
}
