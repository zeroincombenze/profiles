#
# Copyright 2016-25 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
from odoo import SUPERUSER_ID, api


def set_user_lang(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        Users = env["res.users"]
        vals = {
            "country_id": env.ref("base.it").id,
            "tz": "Europe/Rome",
            "lang": env.ref("base.lang_it").code,
        }
        for user in Users.search([]):
            user.partner_id.write(vals)
        del vals["tz"]
        Company = env["res.company"]
        for company in Company.search([]):
            company.partner_id.write(vals)


def set_default_values(cr, registry):
    set_user_lang(cr)
