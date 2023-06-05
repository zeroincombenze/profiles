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

from openerp import models, fields, api, _, tools
import hashlib
import datetime
import time
from openerp.addons.web.http import request


class IrAttachment(models.Model):
    _inherit = 'ir.attachment'

    attachment_url = fields.Char(compute='compute_url', string=_("Attachment URL"))

    @api.one
    def compute_url(self):
        sudo_record = self.sudo()

        unique_id = '%s_%s' % (self.id, hashlib.sha1(sudo_record.write_date or sudo_record.create_date or '').hexdigest()[0:7])
        file_type, ext = self.file_type.split('/')
        if file_type == 'image':
            self.attachment_url = '/external/image/{0}/{1}'.format('ir.attachment', unique_id)
        elif ext == 'pdf':
            self.attachment_url = '/external/pdf/{0}/{1}'.format('ir.attachment', unique_id)

    @api.multi
    def get_response(self, response, cache=None):
        """ Fetches the requested field and ensures it does not go above
        (max_width, max_height), resizing it if necessary.

        Resizing is bypassed if the object provides a $field_big, which will
        be interpreted as a pre-resized version of the base field.

        If the record is not found or does not have the requested field,
        returns a placeholder image via :meth:`~._image_placeholder`.

        Sets and checks conditional response parameters:
        * :mailheader:`ETag` is always set (and checked)
        * :mailheader:`Last-Modified is set iif the record has a concurrency
          field (``__last_update``)

        The requested field is assumed to be base64-encoded image data in
        all cases.
        """

        if not self.ids or not self.mimetype == 'application/pdf':
            return self.env['website']._image_placeholder(response)

        last_update = getattr(self, '__last_update')

        if last_update:
            server_format = tools.misc.DEFAULT_SERVER_DATETIME_FORMAT
            try:
                response.last_modified = datetime.datetime.strptime(
                    last_update, server_format + '.%f')
            except ValueError:
                # just in case we have a timestamp without microseconds
                response.last_modified = datetime.datetime.strptime(
                    last_update, server_format)

        response.set_etag(hashlib.sha1(self.datas).hexdigest())
        response.make_conditional(request.httprequest)

        if cache:
            response.cache_control.max_age = cache
            response.expires = int(time.time() + cache)

        # conditional request match
        if response.status_code == 304:
            return response

        response.mimetype = self.mimetype
        response.headers['Content-Disposition'] = 'inline; filename="%s"' % self.datas_fname
        response.data = self.datas.decode('base64')

        return response
