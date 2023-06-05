# -*- coding: utf-8 -*-
# #############################################################################
#
#    Copyright (C) 2015 Didotech srl (<http://www.didotech.com>)
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

from __future__ import print_function
from openerp import models, fields, api, _


class ProductProduct(models.Model):
    _inherit = 'product.product'

    survey = fields.One2many('product.survey', 'product_id', string=_('Collected Info'))


class ProductSurvey(models.Model):
    _name = 'product.survey'

    _description = 'Survey input collected from customers'

    product_id = fields.Many2one('product.product', string=_('Product'))
    name = fields.Char('Field description', required=True)
    input_type = fields.Selection((
        ('text', _('Text')),
        ('string', _('String')),
        ('checkbox', _('Checkbox')),
        ('number', _('Number')),
        ('selection', _('Selection')),
        ('radio_with_image', _('Radio with image')),
        ('radio_with_text', _('Radio with text'))
    ), string=_('Input type'), required=True)
    radio_image = fields.One2many('ir.attachment', 'res_id',
                                  string=_('Radio Images'), domain=[('res_model', '=', 'product.survey')])
    text_list = fields.One2many('product.survey.textlist', 'survey_id', string="Selection/Radio text")


class ProductSurveyText(models.Model):
    _name = 'product.survey.textlist'

    survey_id = fields.Many2one('product.survey', string=_("Survey"))
    name = fields.Char(_('Text'))
    sequence = fields.Integer(_('Sequence'), help=_("Gives the sequence order when displaying a list of attachment lines."))

    _order = 'sequence'
