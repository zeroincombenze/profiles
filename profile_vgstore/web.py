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

import openerp
from openerp.http import request, STATIC_CACHE, route

import werkzeug.wrappers
import logging
logger = logging.getLogger(__name__)


class eWebsite(openerp.http.Controller):
    def placeholder(self, response):
        return request.registry['website']._image_placeholder(response)

    @route(
        '/external/image/<model>/<record_id>',
        auth="public", website=False)
    def website_image(self, model, record_id, max_width=None, max_height=None):
        """ Fetches the requested field and ensures it does not go above
        (max_width, max_height), resizing it if necessary.

        If the record is not found or does not have the requested field,
        returns a placeholder image via :meth:`~.placeholder`.

        Sets and checks conditional response parameters:
        * :mailheader:`ETag` is always set (and checked)
        * :mailheader:`Last-Modified is set iif the record has a concurrency
          field (``__last_update``)

        The requested field is assumed to be base64-encoded image data in
        all cases.
        """
        response = werkzeug.wrappers.Response()

        if model == 'ir.attachment':
            try:
                idsha = record_id.split('_')
                unique_id = idsha[0]
                return request.registry['website']._image(
                    request.cr, openerp.SUPERUSER_ID, model, unique_id, 'datas', response, max_width, max_height,
                    cache=STATIC_CACHE if len(idsha) > 1 else None)
            except Exception:
                logger.exception("Cannot render image field %r of record %s[%s] at size(%s,%s)",
                                 field, model, record_id, max_width, max_height)
                response = werkzeug.wrappers.Response()
                return self.placeholder(response)
        else:
            return self.placeholder(response)

    @route(
        '/external/pdf/<model>/<record_id>',
         auth="public", website=False)
    def website_pdf(self, model, record_id):
        """ Fetches the requested field.

        If the record is not found or does not have the requested field,
        returns a placeholder image via :meth:`~.placeholder`.

        Sets and checks conditional response parameters:
        * :mailheader:`ETag` is always set (and checked)
        * :mailheader:`Last-Modified is set iif the record has a concurrency
          field (``__last_update``)

        The requested field is assumed to be base64-encoded pdf data in
        all cases.
        """
        response = werkzeug.wrappers.Response()

        if model == 'ir.attachment':
            try:
                idsha = record_id.split('_')
                unique_id = idsha[0]
                # pdb.set_trace()
                unique_id = int(unique_id)
                return request.registry['ir.attachment'].get_response(
                    request.cr, openerp.SUPERUSER_ID, unique_id, response,
                    cache=STATIC_CACHE if len(idsha) > 1 else None)
            except Exception:
                logger.exception("Cannot render pdf field %r of record %s[%s]",
                                 field, model, record_id)
                response = werkzeug.wrappers.Response()
                return self.placeholder(response)
        else:
            return self.placeholder(response)
