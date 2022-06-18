# -*- coding: utf-8 -*-
#
# Copyright 2018-22 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
from odoo import api, SUPERUSER_ID


def set_company_default(cr):
    with api.Environment.manage():
        cr.execute(
            "UPDATE res_company set tax_calculation_rounding_method='round_globally'")


def set_user_zeroadm(cr):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        user = env.ref("base.user_root")
        cr.execute("UPDATE res_users set login='%s' where id=%d" % ("zeroadm", user.id))


def set_default_values(cr, registry):
    set_company_default(cr)
    set_user_zeroadm(cr)
