#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
from odoo import api, SUPERUSER_ID


def set_user_lang(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        user_model = env["res.users"]
        vals = {
            "country_id": env.ref("base.it").id,
            "tz": "Europe/Rome",
            "lang": env.ref("base.lang_it").code,
        }
        for user in user_model.search([]):
            user.partner_id.write(vals)
        company_model = env["res.company"]
        for company in company_model.search([]):
            company.partner_id.write(vals)


def set_default_values(cr, registry):
    set_user_lang(cr)
