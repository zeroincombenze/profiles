# -*- coding: utf-8 -*-
# #############################################################################
#
#    Copyright (C) 2015-2017 Didotech srl (<http://www.didotech.com>)
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
    'name': 'Modulo Profilatura di un Negozio Generico Vampi',
    'version': '4.6.76.8',
    'category': 'Profilazione Clienti',
    'author': 'Didotech SRL',
    'website': 'http://www.didotech.com',
    'license': 'AGPL-3',
    "depends": [
        'base',
        'website_sale',
        # 'sale_stock',
        'product_attachment_gallery',
        'partner_subaccount',
        'restful_backend',
        'delivery',
        'base_partner_always_multi_contacts',
        'product_brand',
        'data_migration',
        'payment_paypal',
        'web_logo',
        'l10n_it_fiscalcode',
        'sale_rpc',
        'product_public_category_order',
        'l10n_it_sale',
        'payment_image',
        'delivery_image',
        'product_public_category_filter'
    ],
    "data": [
        'security/security.xml',
        'views/product_view.xml',
        'views/company_view.xml',
        # 'data/journal.xml',
        # 'report/report_invoice.xml' -> moved to partners profile
        'views/sale_view.xml',
        'views/payment_view.xml',
        #'views/delivery_view.xml'
    ],
    "active": False,
    "installable": True,
    'external_dependencies': {
        'python': []
    }
}
