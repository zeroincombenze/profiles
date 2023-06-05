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

from __future__ import print_function
from openerp import models, fields, api, _
from openerp import exceptions
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT
import time
import requests
import json
import collections

import logging
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

rest_base = 'api'
rest_user = lambda x: x.env.user.company_id.rest_user or 'admin'
rest_pass = lambda x: x.env.user.company_id.rest_pass or 'admin'

DEBUG = False
if DEBUG:
    import pdb


def get_language(code):
    return code[:2]


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    vg_category_id = fields.Integer(_('Vampistore category'))
    product_ids = fields.One2many('product.template', compute='_get_related_products', string='Children Products',
                                  inverse='_write_variants')

    @api.one
    def _get_related_products(self):
        products = self.env['product.template'].search([('public_categ_ids', '=', self.id), ('active', '=', True), ('website_published', '=', True)])
        if products:
            self.product_ids = products.ids
        else:
            self.product_ids = []

    @api.one
    def _write_variants(self):
        pass

    @api.one
    @api.constrains(
        'name',
        'parent_id'
    )
    def unique_name_parent(self):
        if self.search([
                       ('name', '=', self.name),
                       ('parent_id', '=', self.parent_id and self.parent_id.id or False),
                       ('id', '!=', self.id)]):
            raise exceptions.Warning(_("Category '{name}' already exists").format(name=self.name))
        else:
            return True

    def is_duplicate(self, name, parent_id):
        duplicate = self.search([
            ('name', '=', name),
            ('parent_id', '=', parent_id),
            # ('id', '!=', self.id)
        ])
        if duplicate:
            return duplicate[0]
        else:
            return False

    @api.multi
    def is_menu(self):
        # This line generates error when program is not launched from command line
        # print('M >>', self.name, self.parent_id and self.parent_id.name or 'orfan')
        if self.parent_id:
            if self.parent_id.id == self.get_menu_id():
                print(u'True, my parent is menu', self.name)
                return True
            elif self.parent_id.parent_id:
                return self.parent_id.is_menu()
            else:
                return False
        elif self.id == self.get_menu_id():
            print(u'True, I am menu', self.name)
            return True
        else:
            return False

    @api.model
    def get_menu(self):
        menu = self.with_context(strict=True).search([('parent_id', '=', False), ('name', '=ilike', '_menu')])
        if menu:
            return menu[0]
        else:
            return self.create({
                'parent_id': False,
                'name': '_Menu',
                'vg_category_id': 0,
            })

    @api.model
    def get_menu_id(self):
        return self.get_menu().id

    @api.model
    def create(self, values):
        print(u'CREATE:', values)

        if values.get('parent_id'):
            parent = self.browse(values['parent_id'])
        elif values.get('from_vgstore'):
            parent = self.get_menu()
            values['parent_id'] = parent.id
        else:
            parent = False

        # if parent:
        #     print('PPPPPPP>', parent.name)

        if parent and parent.is_menu():
            print(u'Parent IS MENU:', parent.name, values)

            if self.env.user.company_id.django_host:
                if values.get('from_vgstore'):
                    del values['from_vgstore']
                    create_in_vgstore = False
                else:
                    create_in_vgstore = True

                duplicate = self.is_duplicate(values['name'], values.get('parent_id'))
                if duplicate:
                    category = duplicate[0]
                else:
                    category = super(ProductPublicCategory, self).create(values)

                if create_in_vgstore:
                    values['odoo_category'] = category.id
                    _logger.info(u'==================== >>> Creating {} in VGStore...'.format(values['name']))
                    # print(values)

                    response = self.vg7_create(values)
                    if response.status_code in (201, 302):
                        self.env.cr.commit()
                        if response.json().get('pk'):
                            category.write({
                                'vg_category_id': response.json()['pk'],
                                'from_vgstore': True
                            })
                return category
            else:
                raise exceptions.Warning('Please set Django Host \n'
                                         '(Configuration -> Company -> Django Host -> Your Company)\n'
                                         '(Configurazione -> Aziende -> Aziende -> Your Company)')
        else:
            return super(ProductPublicCategory, self).create(values)

    def vg7_create(self, values):
        if values.get('parent_id'):
            parent = self.browse(values['parent_id'])
            vg_parent_id = parent.vg_category_id
        elif values.get('vg_parent_id'):
            vg_parent_id = values['vg_parent_id']
        else:
            vg_parent_id = ''

        print(values)

        # create category in VG Store
        payload = json.dumps({
            'title': values['name'],
            'index': values.get('sequence', 0),
            'parent': vg_parent_id,
            'odoo_category': values['odoo_category'],
            'no_odoo': True
        })

        headers = {'content-type': 'application/json'}

        # TODO: Verify that user has rights to create categories
        return requests.post(
            'http://{host}/{language_code}/{rest_base}/sections/'.format(
                host=self.env.user.company_id.django_host,
                language_code=get_language(self._context.get('lang')),
                rest_base=rest_base),
            auth=(rest_user(self), rest_pass(self)),
            headers=headers,
            data=payload
        )

    @api.multi
    def write(self, values):
        print(u'WRITE:', values)

        if values.get('from_vgstore'):
            del values['from_vgstore']
            if not values.get('parent_id') and not self.parent_id:
                values['parent_id'] = self.get_menu_id()
            elif 'parent_id' in values:
                del values['parent_id']
        elif self.is_menu():
            if self.env.user.company_id.django_host:
                for category in self:
                    if category.vg_category_id:
                        if values.get('name') and len(values) == 1:
                            payload = {
                                'title': values['name'],
                                'no_odoo': True
                            }
                            headers = {'content-type': 'application/json'}
                            # TODO: Verify that user has rights to modify categories
                            response = requests.patch(
                                'http://{host}/{language_code}/{rest_base}/sections/{category_id}/'.format(
                                    host=self.env.user.company_id.django_host,
                                    category_id=self.vg_category_id,
                                    language_code=get_language(self._context.get('lang')),
                                    rest_base=rest_base
                                ),
                                auth=(rest_user(self), rest_pass(self)),
                                headers=headers,
                                data=json.dumps(payload)
                            )
                            # print('>>>> Status:', response.status_code)

                        else:
                            # {'name', 'parent_id', 'index'}.intersection(values.keys()):
                            # modify category in VG Store
                            payload = {
                                'index': values.get('sequence', category.sequence or 0),
                                'odoo_category': category.id,
                                'no_odoo': True,
                                'title': values.get('name', category.name)
                            }

                            if values.get('parent_id') and not values['parent_id'] == self.get_menu_id():
                                parent = self.browse(values['parent_id'])

                                if parent and parent.vg_category_id:
                                    payload['parent'] = parent.vg_category_id
                                else:
                                    # Abnormal situation, we are out of sync
                                    # TODO: Decide what to do
                                    payload['parent'] = ''
                            elif self.parent_id and not self.parent_id.id == self.get_menu_id():
                                payload['parent'] = self.parent_id.vg_category_id
                            else:
                                payload['parent'] = ''

                            headers = {'content-type': 'application/json'}
                            # TODO: Verify that user has rights to modify categories
                            response = requests.put(
                                'http://{host}/{language_code}/{rest_base}/sections/{category_id}/'.format(
                                    host=self.env.user.company_id.django_host,
                                    category_id=self.vg_category_id,
                                    language_code=get_language(self._context.get('lang')),
                                    rest_base=rest_base
                                ),
                                auth=(rest_user(self), rest_pass(self)),
                                headers=headers,
                                data=json.dumps(payload)
                            )

                        # print('>>>> Status:', response.status_code)
                        if response.status_code == 404:
                            # It means we are out of sync with VG7
                            response2 = self.vg7_create({
                                'name': values.get('name') or category.name,
                                'sequence': values.get('sequence', category.sequence or ''),
                                'parent_id': category.parent_id and category.parent_id.id or '',
                                'odoo_category': category.id,
                                'no_odoo': True
                            })

                            if response2.status_code in (201, 302):
                                if response2.json().get('pk'):
                                    category.write({
                                        'vg_category_id': response2.json()['pk'],
                                        'from_vgstore': True
                                    })
                        elif response.status_code == 400:
                            raise exceptions.ValidationError("Bad request")
                        elif response.status_code == 500:
                            raise exceptions.ValidationError(
                                "({category.id}: {category.name}) Django: Internal Server Error".format(category=category)
                            )
                        elif not response.status_code in (200, 201, 302):
                            raise exceptions.Warning(
                                'VG Server returned an error {}'.format(response.status_code)
                            )
            else:
                raise exceptions.Warning('Please set Django Host \n'
                                         '(Configuration -> Company -> Django Host -> Your Company)\n'
                                         '(Configurazione -> Aziende -> Aziende -> Your Company)')
        return super(ProductPublicCategory, self).write(values)

    @api.one
    def unlink(self):
        if self._context.get('from_vgstore') or not self.vg_category_id:
            return super(ProductPublicCategory, self).unlink()
        else:
            if self.env.user.company_id.django_host:
                headers = {'content-type': 'application/json'}

                payload = {
                    'no_odoo': True,
                }

                # TODO: Verify that user has rights to delete categories
                response = requests.delete(
                    'http://{host}/{rest_base}/sections/{category_id}/'.format(
                        host=self.env.user.company_id.django_host,
                        category_id=self.vg_category_id,
                        rest_base=rest_base
                    ),
                    auth=(rest_user(self), rest_pass(self)),
                    headers=headers,
                    data=json.dumps(payload)
                )

                if response.status_code in (200, 404):
                    return super(ProductPublicCategory, self).unlink()
                else:
                    raise exceptions.Warning(response.json().get('error') or response.json().get('status'))
            else:
                raise exceptions.Warning('Please set Django Host \n'
                                         '(Configuration -> Company -> Django Host -> Your Company)\n'
                                         '(Configurazione -> Aziende -> Aziende -> Your Company)')

    @api.multi
    def sync_all(self):
        errors = []

        root_menu_id = self.get_menu_id()

        headers = {'content-type': 'application/json'}

        if self._context.get('active_ids'):
            categories = self.search([('id', 'in', self._context['active_ids'])])
        else:
            # set in_sync flag to False
            requests.post(
                'http://{host}/{language_code}/{rest_base}/sections/sync/false/'.format(
                    host=self.env.user.company_id.django_host,
                    language_code=get_language(self._context.get('lang')),
                    rest_base=rest_base),
                auth=(rest_user(self), rest_pass(self)),
                headers=headers,
                data={}
            )

            categories = self.with_context({'strict': True}).search([])

        for counter, category in enumerate(categories):
            if not category.id == root_menu_id and category.is_menu():
                vg_parent_id = category.parent_id and category.parent_id.vg_category_id or ''

                # create product in VG Store
                payload = json.dumps({
                    'title': category.name,
                    'odoo_category': category.id,
                    'parent': vg_parent_id,
                    'no_odoo': True,
                    'index': category.sequence or ''
                })

                # print('-------------->', counter, category.name)

                if category.vg_category_id:
                    # TODO: Verify that user has rights to create products
                    _logger.info(u'Category ID:', category.vg_category_id, u'Title: ', category.name)
                    response = requests.put(
                        'http://{host}/{language_code}/{rest_base}/sections/{category_id}/'.format(
                            host=self.env.user.company_id.django_host,
                            language_code=get_language(self._context.get('lang')),
                            category_id=category.vg_category_id,
                            rest_base=rest_base),
                        auth=(rest_user(self), rest_pass(self)),
                        headers=headers,
                        data=payload
                    )
                else:
                    # TODO: Verify that user has rights to create products
                    response = requests.post(
                        'http://{host}/{language_code}/{rest_base}/sections/'.format(
                            host=self.env.user.company_id.django_host,
                            language_code=get_language(self._context.get('lang')),
                            rest_base=rest_base),
                        auth=(rest_user(self), rest_pass(self)),
                        headers=headers,
                        data=payload
                    )

                if response.status_code in (201, ):
                    # category created, update category
                    category.write({
                        'vg_category_id': response.json()['pk'],
                        'from_vgstore': True
                    })
                elif response.status_code == 302:
                    # Category already present
                    content = json.loads(response.content)
                    category.vg_category_id = content.get('pk', 0)
                    if content.get('status'):
                        _logger.warning(content['status'])

                if response.status_code not in (200, 201, 302, 404):
                    if response.json().get('error'):
                        errors.append(category.name + ' ' + response.json()['error'])
                    else:
                        errors.append(category.name)

                # Sync other languages:
                for language in self.env['res.lang'].get_available_languages():
                    if not language.code == self._context.get('lang'):
                        payload = {
                            'title': category.with_context({'lang': language.code}).name,
                            'no_odoo': True
                        }

                        print('LANGUAGE:', language.code)
                        print(payload)

                        # TODO: Verify that user has rights to modify categories
                        response = requests.patch(
                            'http://{host}/{language_code}/{rest_base}/sections/{category_id}/'.format(
                                host=self.env.user.company_id.django_host,
                                category_id=category.vg_category_id,
                                language_code=language.get_iso_code(),
                                rest_base=rest_base
                            ),
                            auth=(rest_user(self), rest_pass(self)),
                            headers=headers,
                            data=json.dumps(payload)
                        )

                        if response.status_code not in (200, 302):
                            if response.json().get('error'):
                                errors.append(category.name + ' ' + response.json()['error'])
                            else:
                                errors.append(category.name)

        if errors:
            return False
        else:
            if not self._context.get('active_ids'):
                # delete unsynced
                response = requests.delete(
                    'http://{host}/{language_code}/{rest_base}/sections/sync/clean/'.format(
                        host=self.env.user.company_id.django_host,
                        language_code=get_language(self._context.get('lang')),
                        rest_base=rest_base),
                    auth=(rest_user(self), rest_pass(self)),
                    headers=headers,
                    data={}
                )
                if response.status_code not in (200, 302):
                    if response.json().get('error'):
                        raise exceptions.Warning(response.json()['error'])
                    else:
                        raise exceptions.Warning(_('Error: Sync failed'))

            return True

    @api.model
    def children_search(self, parents, offset=0, limit=0, order=None, count=False):
        children = super(ProductPublicCategory, self).search([('parent_id', 'in', parents.ids)])
        if children:
            return children + self.children_search(children, offset=offset, limit=limit, order=order, count=count)
        else:
            return children

    # Disabled because it is very slow!!!
    # @api.model
    # def search(self, args, offset=0, limit=0, order=None, count=False, strict=False):
    #     categories = super(ProductPublicCategory, self).search(args, offset=offset, limit=False, order=order, count=count)
    #     if args and categories and not strict:
    #         categories += self.children_search(categories, offset=offset, limit=limit, order=order, count=count)
    #     return categories

    def search(self, cr, uid, args, offset=0, limit=0, order=None, count=False, context=None):
        strict = context and context.get('strict', False) or False

        category_ids = super(ProductPublicCategory, self).search(cr, uid, args, offset=offset, limit=False, order=order, count=count, context=context)

        # 'parent_id' creates problems for reverse mapping child_id.
        # (function get() of one2many field)
        if args and category_ids and not strict and not 'parent_id' in args[0]:
            categories = self.browse(cr, uid, category_ids, context)
            categories += self.children_search(cr, uid, categories, offset=offset, limit=limit, order=order, count=count, context=context)
            return categories.ids
        else:
            return category_ids

    @api.multi
    def name_tree(self):
        id_tree = collections.deque([(self.id, self.name)])
        category = self

        while category.parent_id:
            id_tree.appendleft((category.parent_id.id, category.parent_id.name))
            category = category.parent_id

        return list(id_tree)

    @api.model
    def get_associated_categories(self, category_id):
        # Get all categories which products from category_id has
        self._cr.execute("""
            SELECT templ.product_public_category_id, product_public_category.name
            FROM product_public_category_product_template_rel AS product
            LEFT JOIN product_public_category_product_template_rel AS templ
            ON product.product_template_id=templ.product_template_id
            LEFT JOIN product_public_category
            ON product_public_category.id=templ.product_public_category_id
            WHERE product.product_public_category_id={0}
            AND templ.product_public_category_id!={0}
            GROUP BY templ.product_public_category_id, product_public_category.name
        """.format(category_id))

        categories = {}
        for row in self._cr.dictfetchall():
            parents = self.get_parents(row['product_public_category_id'], [])

            root_category = parents.pop()
            level = 0
            if root_category['id'] not in categories:
                categories[root_category['id']] = {
                    'name': root_category['name'],
                    'children': {},
                    'level': level
                }

            category = categories[root_category['id']]

            while parents:
                parent = parents.pop()
                level += 1

                if parent['id'] not in category['children']:
                    category['children'][parent['id']] = {
                        'name': parent['name'],
                        'children': {},
                        'level': level
                    }

                category = category['children'][parent['id']]

            if 'depth' in categories[root_category['id']] and categories[root_category['id']]['depth'] < level + 1 \
                    or 'depth' not in categories[root_category['id']]:
                categories[root_category['id']]['depth'] = level + 1

        return json.dumps(categories)

    def get_parents(self, category_id, stack):
        self._cr.execute("""
            SELECT id, name, parent_id
            FROM product_public_category
            WHERE id={}
        """.format(category_id))
        category = self._cr.dictfetchone()

        stack.append(category)
        if category['parent_id']:
            self.get_parents(category['parent_id'], stack)

        return stack


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    vg_product_id = fields.Integer(_('Vampistore product'))
    sequence = fields.Integer(_('Sequence'))

    _order = 'sequence, name'

    @api.model
    def create(self, values):
        if self.env.user.company_id.django_host:
            if values.get('from_vgstore'):
                del values['from_vgstore']
                create_in_vgstore = False
            else:
                create_in_vgstore = True

            print(u'################### Create: ', values)

            if values.get('odoo_product'):
                # This should never happen
                raise exceptions.Warning("Circular product creation")
                # product = self.browse(values['odoo_product'])
                # return product
            else:
                product_template = super(ProductTemplate, self).create(values)

            if create_in_vgstore:
                values['odoo_product'] = product_template.id
                values['name'] = product_template.name
                response = self.vg7_create(values)
                if response.status_code in (201, 302):
                    self.env.cr.commit()
                    print('OK, product in VGStore created')
                    if response.json().get('pk'):
                        product_template.write({
                            'vg_product_id': response.json()['pk'],
                            'from_vgstore': True
                        })

            return product_template
        else:
            raise exceptions.Warning('Please set Django Host \n'
                                     '(Configuration -> Company -> Django Host -> Your Company)\n'
                                     '(Configurazione -> Aziende -> Aziende -> Your Company)')

    def vg7_create(self, values):
        print(values)

        if values.get('public_categ_ids'):
            category = self.get_public_category(values['public_categ_ids'])
            if category:
                parent = category and self.env['product.public.category'].browse(category)
                vg_parent_id = parent.vg_category_id
            else:
                vg_parent_id = ''
        elif values.get('vg_parent_id'):
            vg_parent_id = values['vg_parent_id']
        else:
            vg_parent_id = ''

        # create product in VG Store
        payload = json.dumps({
            'title': values['name'],
            'odoo_product': values['odoo_product'],
            'parent': vg_parent_id,
            'no_odoo': True,
            'is_active': values.get('is_active')
        })

        print(u'-------------->', payload)

        headers = {'content-type': 'application/json'}

        # TODO: Verify that user has rights to create products
        return requests.post(
            'http://{host}/{language_code}/{rest_base}/products/'.format(
                host=self.env.user.company_id.django_host,
                language_code=get_language(self._context.get('lang')),
                rest_base=rest_base
            ),
            auth=(rest_user(self), rest_pass(self)),
            headers=headers,
            data=payload
        )

    @staticmethod
    def get_public_category(categories):
        for category in categories:
            if category[0] in (1, 4):
                return category[1]
            elif category[0] == 6 and category[2]:
                return category[2][0]
        return False

    @api.multi
    def write(self, values):
        print(u'WRITE:', values)

        vg_fields = ('name', 'odoo_product', 'parent', 'website_published', 'sequence')

        if values.get('from_vgstore'):
            del values['from_vgstore']
        elif self.id and set(vg_fields).intersection(values):
            if self.env.user.company_id.django_host:
                for product in self:
                    if product.vg_product_id:
                        # modify product in VG Store
                        if values.get('name') and len(values) == 1:
                            payload = {
                                'title': values['name'],
                                'no_odoo': True
                            }
                            headers = {'content-type': 'application/json'}
                            # TODO: Verify that user has rights to modify products
                            response = requests.patch(
                                'http://{host}/{language_code}/{rest_base}/products/{product_id}/'.format(
                                    host=self.env.user.company_id.django_host,
                                    product_id=self.vg_product_id,
                                    language_code=get_language(self._context.get('lang') or self.env.user.lang),
                                    rest_base=rest_base
                                ),
                                auth=(rest_user(self), rest_pass(self)),
                                headers=headers,
                                data=json.dumps(payload)
                            )
                            # print('>>>> Status:', response.status_code)
                        else:
                            payload = {
                                'odoo_product': product.id,
                                'no_odoo': True
                            }

                            if 'name' in values:
                                payload['title'] = values['name']

                            if 'website_published' in values:
                                payload['is_active'] = values['website_published']

                            if values.get('public_categ_ids'):
                                category = self.get_public_category(values['public_categ_ids'])
                                parent = category and self.env['product.public.category'].browse(category)

                                if parent and parent.vg_category_id:
                                    payload['parent'] = parent.vg_category_id
                                else:
                                    # Abnormal situation, we are out of sync
                                    _logger.warning(
                                        u"Abnormal situation, Product Public Category {category.id} '{category.name}' is out of sync".format(
                                            category=parent
                                        )
                                    )
                                    if DEBUG:
                                        pdb.set_trace()

                                    payload['parent'] = self.get_menu_category()
                            else:
                                payload['parent'] = self.get_menu_category()

                            if 'sequence' in values:
                                payload['index'] = values['sequence'] or 0

                            headers = {'content-type': 'application/json'}
                            # TODO: Verify that user has rights to modify products
                            response = requests.put(
                                'http://{host}/{language_code}/{rest_base}/products/{product_id}/'.format(
                                    host=self.env.user.company_id.django_host,
                                    product_id=self.vg_product_id,
                                    language_code=get_language(self._context.get('lang') or self.env.user.lang),
                                    rest_base=rest_base
                                ),
                                auth=(rest_user(self), rest_pass(self)),
                                headers=headers,
                                data=json.dumps(payload)
                            )
                        # print('>>>> Status:', response.status_code)
                        if response.status_code == 404:
                            # It means we are out of sync with VG7
                            response2 = self.vg7_create({
                                'name': product.name,
                                'odoo_product': product.id,
                                'vg_parent_id': product.public_categ_ids and product.public_categ_ids[0].vg_category_id or '',
                                'no_odoo': True
                            })

                            if response2.status_code in (201, 302):
                                if response2.json().get('pk'):
                                    product.write({
                                        'vg_product_id': response2.json()['pk'],
                                        'from_vgstore': True,
                                    })
                        elif response.status_code == 400:
                            raise exceptions.ValidationError("Bad request")
                        elif response.status_code == 500:
                            raise exceptions.Warning("Django: Internal Server Error")
                        elif not response.status_code == 200:
                            raise exceptions.Warning('VG Server returned an error', response.json().get('error') or response.json().get('status'))
                    else:
                        # It means we are out of sync with VG7
                        response2 = self.vg7_create({
                            'name': product.name,
                            'odoo_product': product.id,
                            'vg_parent_id': product.public_categ_ids and product.public_categ_ids[0].vg_category_id or '',
                            'no_odoo': True
                        })

                        if response2.status_code in (201, 302):
                            if response2.json().get('pk'):
                                product.write({
                                    'vg_product_id': response2.json()['pk'],
                                    'from_vgstore': True,
                                })
            else:
                raise exceptions.Warning('Please set Django Host \n'
                                         '(Configuration -> Company -> Django Host -> Your Company)\n'
                                         '(Configurazione -> Aziende -> Aziende -> Your Company)')

        return super(ProductTemplate, self).write(values)

    @api.one
    def unlink(self):
        if self._context.get('from_vgstore') or not self.vg_product_id:
            return super(ProductTemplate, self).unlink()
        else:
            if self.env.user.company_id.django_host:
                headers = {'content-type': 'application/json'}

                payload = {
                    'no_odoo': True,
                }

                # TODO: Verify that user has rights to delete products
                response = requests.delete(
                    'http://{host}/{rest_base}/products/{product_id}/'.format(
                        host=self.env.user.company_id.django_host,
                        product_id=self.vg_product_id,
                        rest_base=rest_base
                    ),
                    auth=(rest_user(self), rest_pass(self)),
                    headers=headers,
                    data=json.dumps(payload)
                )

                if response.status_code in (200, 404):
                    return super(ProductTemplate, self).unlink()
                else:
                    raise exceptions.Warning(response.json().get('error') or response.json().get('status'))
            else:
                raise exceptions.Warning('Please set Django Host \n'
                                         '(Configuration -> Company -> Django Host -> Your Company)\n'
                                         '(Configurazione -> Aziende -> Aziende -> Your Company)')

    @api.one
    def get_price(self, customer=False, partner_id=False, quantity=1.0):
        if customer or partner_id:
            if customer:
                users = self.env['res.users'].search([('login', '=', customer)])
                if users:
                    partner = users and users.partner_id
                else:
                    # Unknown customer (registered in Django, but not in Odoo)
                    return False
            else:
                partner = self.env['res.partner'].browse(partner_id)

            product = self.env['product.product'].search([('product_tmpl_id', '=', self.id)])

            if len(product) > 1:
                # TODO: This is OK until we are not dealing with variants
                # (if there is a possibility that variants has different price)
                prod_id = product.ids[0]
            else:
                prod_id = product.id

            prices = partner.property_product_pricelist.price_get(
                prod_id=prod_id,
                qty=quantity,
                partner=partner.id,
                context={
                    'uom': self.uom_id.id,
                    'date': time.strftime(DEFAULT_SERVER_DATE_FORMAT),
                }
            )
            price = prices[partner.property_product_pricelist.id]
        else:
            price = False

        return price or self.list_price

    def get_prices(self, cr, uid, results, customer, quantity, context):
        for product_template_data in results:
            product_template = self.browse(cr, uid, product_template_data['pk'], context)
            for product in product_template_data['product_variant_ids']:
                prices = product_template.get_price(customer=customer, quantity=quantity)
                product['list_price'] = prices and prices[0]
        return results

    @api.model
    def get_products_with_prices(self, template_id, customer, quantity):
        data = json.loads(self.env['rest.ful'].get(template_id))
        if data:
            data['results'] = self.get_prices(data['results'], customer=customer, quantity=quantity)
        else:
            data = {}
        return json.dumps(data)

    @api.model
    def get_menu_category(self):
        for category in self.public_categ_ids:
            if category.is_menu():
                return category.vg_category_id
        else:
            return ''

    @api.multi
    def sync_all(self):
        errors = []

        headers = {'content-type': 'application/json'}

        if self._context.get('active_ids'):
            # sync active products
            products = self.browse(self._context['active_ids'])
        else:
            # set in_sync flag to False
            requests.post(
                'http://{host}/{language_code}/{rest_base}/products/sync/false/'.format(
                    host=self.env.user.company_id.django_host,
                    language_code=get_language(self._context.get('lang')),
                    rest_base=rest_base),
                auth=(rest_user(self), rest_pass(self)),
                headers=headers,
                data={}
            )
            # sync all products
            products = self.search([('sale_ok', '=', True)])

        for counter, t_product in enumerate(products):
            for category in t_product.public_categ_ids:
                if category.is_menu():
                    vg_parent_id = category.vg_category_id
                    break
                # vg_parent_id = t_product.public_categ_ids[0].vg_category_id
            else:
                vg_parent_id = ''

            # create product in VG Store
            payload = json.dumps({
                'title': t_product.name,
                'odoo_product': t_product.id,
                'parent': vg_parent_id,
                'no_odoo': True,
                'index': t_product.sequence or 0
            })

            # print('-------------->', counter, t_product.name)

            if t_product.vg_product_id:
                # TODO: Verify that user has rights to create products
                response = requests.put(
                    'http://{host}/{language_code}/{rest_base}/products/{product_id}/'.format(
                        host=self.env.user.company_id.django_host,
                        product_id=t_product.vg_product_id,
                        language_code=get_language(self._context.get('lang')),
                        rest_base=rest_base),
                    auth=(rest_user(self), rest_pass(self)),
                    headers=headers,
                    data=payload
                )
            else:
                # TODO: Verify that user has rights to create products
                response = requests.post(
                    'http://{host}/{language_code}/{rest_base}/products/'.format(
                        host=self.env.user.company_id.django_host,
                        language_code=get_language(self._context.get('lang')),
                        rest_base=rest_base),
                    auth=(rest_user(self), rest_pass(self)),
                    headers=headers,
                    data=payload
                )

            if response.status_code in (201, ):
                # product created, update t_product
                t_product.write({
                    'vg_product_id': response.json()['pk'],
                    'from_vgstore': True
                })

            if response.status_code not in (200, 201, 302, 404):
                if response.status_code == 500:
                    raise exceptions.Warning(t_product.name + ' Django: Internal Server Error')
                elif response.json().get('error'):
                    errors.append(t_product.name + ' ' + response.json()['error'])
                else:
                    errors.append(t_product.name)

            # Sync other languages:
            for language in self.env['res.lang'].get_available_languages():
                if not language.code == self._context.get('lang'):
                    payload = {
                        'title': t_product.with_context({'lang': language.code}).name,
                        'no_odoo': True
                    }
                    headers = {'content-type': 'application/json'}
                    # TODO: Verify that user has rights to modify categories
                    response = requests.patch(
                        'http://{host}/{language_code}/{rest_base}/products/{product_id}/'.format(
                            host=self.env.user.company_id.django_host,
                            product_id=t_product.vg_product_id,
                            language_code=language.get_iso_code(),
                            rest_base=rest_base
                        ),
                        auth=(rest_user(self), rest_pass(self)),
                        headers=headers,
                        data=json.dumps(payload)
                    )

                    if response.status_code not in (200, 302):
                        if response.status_code == 500:
                            raise exceptions.Warning(t_product.name + ' Django: Internal Server Error')
                        elif response.json().get('error'):
                            errors.append(t_product.name + ' ' + response.json()['error'])
                        else:
                            errors.append(t_product.name)

        if errors:
            return False
        else:
            if not self._context.get('active_ids'):
                # delete unsynced
                response = requests.delete(
                    'http://{host}/{language_code}/{rest_base}/products/sync/clean/'.format(
                        host=self.env.user.company_id.django_host,
                        language_code=get_language(self._context.get('lang')),
                        rest_base=rest_base),
                    auth=(rest_user(self), rest_pass(self)),
                    headers=headers,
                    data={}
                )
                if response.status_code not in (200, 302):
                    if response.status_code == 500:
                        raise exceptions.Warning('Cleaning: Django: Internal Server Error')
                    else:
                        # elif response.json().get('error'):
                        # raise exceptions.Warning(response.json()['error'])

                        # raise exceptions.Warning(_('Error: Sync failed'))
                        raise exceptions.Warning(_("Unable to clean products. Status: {status}").format(status=response.status_code))

            return True

    @api.multi
    def get_product(self):
        headers = {'content-type': 'application/json'}

        if self.vg_product_id:
            response = requests.get(
                'http://{host}/{rest_base}/products/{product_id}/'.format(
                    host=self.env.user.company_id.django_host,
                    product_id=self.vg_product_id,
                    rest_base=rest_base
                ),
                auth=(rest_user(self), rest_pass(self)),
                headers=headers,
                # data=json.dumps(payload)
            )

            if response.status_code == 200:
                return True
            else:
                return False
        else:
            return False

    @api.multi
    def verify_products(self):
        out_of_sync = []

        for product in self.search([('sale_ok', '=', True)]):
            if not product.get_product():
                out_of_sync.append(product.id)

        return {
            'type': 'ir.actions.act_window',
            'name': _('Unsynced Products'),
            'res_model': 'product.template',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'view_id': False,
            'target': 'current',
            'res_id': False,
            "domain": [('id', 'in', out_of_sync)]
        }

    @api.multi
    def variants_attributes_list(self):
        variants_attributes = []
        for product in self.product_variant_ids:
            variants_attributes += [(value.id, value.attribute_id.name, value.name, value.attribute_id.id) for value in product.attribute_value_ids]

        unique_attributes = list(set(variants_attributes))
        return [{'pk': attribute[0], attribute[1]: attribute[2], 'kei_pk': attribute[3]} for attribute in unique_attributes]

    @api.multi
    def taxes(self):
        return [
            {
                'name': tax.name,
                'value': tax.type == 'percent' and int(tax.amount * 100) or int(tax.amount),
                'type': tax.type
            } for tax in self.taxes_id
        ]

    # # Present problems with more than 80 results, very slow
    # @api.model
    # def search(self, args, offset=0, limit=0, order=None, count=False):
        # for arg in args:
        #     if arg and len(arg) == 3 and arg[0] == 'attrib' and '__' in arg[2]:
        #         attrib, value = arg[2].split('__', 1)
        #         if attrib.isdigit() and value.isdigit():
        #             products = self.env['product.product'].search([
        #                 ('attribute_value_ids.id', '=', value),
        #                 ('attribute_value_ids.attribute_id.id', '=', attrib)
        #             ])
        #         else:
        #             products = self.env['product.product'].search([
        #                 ('attribute_value_ids.name', '=', value),
        #                 ('attribute_value_ids.attribute_id.name', '=', attrib)
        #             ])
        #         if products:
        #             arg[0] = 'id'
        #             arg[1] = 'in'
        #             arg[2] = [product.product_tmpl_id.id for product in products]

        # return super(ProductTemplate, self).search(args, offset=offset, limit=limit, order=order, count=count)

    def search(self, cr, uid, args, offset=0, limit=0, order=None, context=None, count=False):
        for arg in args:
            if arg and len(arg) == 3 and arg[0] == 'attrib' and '__' in arg[2]:
                attrib, value = arg[2].split('__', 1)
                if attrib.isdigit() and value.isdigit():
                    products = self.pool['product.product'].search(cr, uid, [
                        ('attribute_value_ids.id', '=', value),
                        ('attribute_value_ids.attribute_id.id', '=', attrib)
                    ])
                else:
                    products = self.pool['product.product'].search(cr, uid, [
                        ('attribute_value_ids.name', '=', value),
                        ('attribute_value_ids.attribute_id.name', '=', attrib)
                    ])
                if products:
                    arg[0] = 'id'
                    arg[1] = 'in'
                    arg[2] = [product.product_tmpl_id.id for product in products]

        return super(ProductTemplate, self).search(cr, uid, args, offset=offset, limit=limit, order=order, count=count, context=context)

    @api.model
    def price_search(self, values):
        """
        Search among taxed prices
        """

        query = """SELECT p_d.prod_id, p_d.tax_id, tax.type, tax.name, tax.amount, p.name, p.list_price, (tax.amount + 1) * p.list_price AS taxed_price
        FROM product_taxes_rel AS p_d
        LEFT JOIN account_tax AS tax
        ON p_d.tax_id = tax.id
        LEFT JOIN product_template AS p
        ON p_d.prod_id = p.id
        WHERE tax.type = 'percent'
        AND (tax.amount + 1) * p.list_price {lookup_type} {value}
        ORDER BY taxed_price""".format(lookup_type=values['lookup_type'], value=values['value'])

        self._cr.execute(query)
        return [row['prod_id'] for row in self._cr.dictfetchall()]