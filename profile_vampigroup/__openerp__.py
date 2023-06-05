# -*- coding: utf-8 -*-
# #############################################################################
#
#    Copyright (C) 2015-2016 Didotech srl (<http://www.didotech.com>)
#    All Rights Reserved
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

{
    'name': 'Modulo Profilatura di Vampigroup',
    'version': '4.1.5.18',
    'category': 'Profilazione Clienti',
    'description': """
Modulo Profilatura di Vampigroup
================================

modulo aggiunge funzionalita ed installa i moduli necessari
    """,
    'author': 'Didotech SRL',
    'website': 'http://www.didotech.com',
    'license': 'AGPL-3',
    "depends": [
        'base',
        'sale',
        # 'website_sale',
        # # 'sale_stock',
        # 'product_attachment_gallery',
        # 'partner_subaccount',
        # 'restful_backend',
        # 'delivery',
        # 'base_partner_always_multi_contacts',
        # 'product_brand',
        # 'data_migration',
        # 'payment_paypal',
        'web_logo',
        'account_analytic_analysis',    # Contracts Management
        'delivery',
        'account_invoice_due_dates',
        'l10n_it_sale',
        'sale_plus',
        'partner_extended',
        'account_invoice_plus'
    ],
    "data": [
        # 'report/paper_format.xml',
        # 'report/report_invoice.xml',
        # 'report/report_sale.xml',
        # 'report/report_picking.xml',
        # 'views/account_view.xml',
        # 'views/sale_order_view.xml',
        # 'views/company_view.xml',
        # 'views/product_view.xml'
    ],
    "active": False,
    "installable": True,
    'external_dependencies': {
        'python': []
    }
}
