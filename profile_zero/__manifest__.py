#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
{
    "name": "profile zeroincombenze(R)",
    "version": "12.0.1.0.3",
    "category": "Technical Settings",
    "summary": "Zeroincombenze Setup",
    "author": "SHS-AV s.r.l.",
    "website": "https://www.zeroincombenze.it",
    "development_status": "Beta",
    "license": "AGPL-3",
    "depends": [
        "profile_common",
        "profile_base",
        "profile_account",
        "profile_payment",
        "profile_sale",
    ],
    "maintainer": "Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>",
    "installable": True,
    'post_init_hook': 'set_default_values',
}
