# -*- coding: utf-8 -*-
#
# Copyright 2018-21 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
#
from openerp import pooler, SUPERUSER_ID

def migrate(cr, version):
    """Migration entry point

    :param cr: Database Cursor
    :param version: Odoo and module versions
    """
    if version is None:
        return
    lang = 'it_IT'

    model_name = 'res.lang'
    lang_model = pooler.get_pool(cr.dbname)[model_name]
    cr.execute(
        "SELECT id FROM res_lang WHERE code = '%s'" % lang
    )
    lang_id = cr.fetchall()[0][0]
    lang_model.write(
        cr, SUPERUSER_ID, lang_id, {'active': True}
    )

    model_name = 'base.language.install'
    lang_install_model = pooler.get_pool(cr.dbname)[model_name]
    vals = {
        'lang': lang,
        'overwrite': True,
    }
    id = lang_install_model.create(cr, SUPERUSER_ID, vals)
    lang_install_model.lang_install([id])
