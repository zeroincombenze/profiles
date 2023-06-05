# -*- coding: utf-8 -*-
# #############################################################################
#
#    Copyright (C) 2015 Didotech srl (<http://www.didotech.com>)
#
#                       All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

from openerp import models, fields, api, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    django_host = fields.Char(_('Django Host'), help="""Django host accessible via RESTful API in formato host:port""")
    rest_user = fields.Char(_('Django/Odoo admin user'), help="""Django and Odoo admin user""")
    rest_pass = fields.Char(_('Django/Odoo admin password'), help="""Django and Odoo admin's password""")
