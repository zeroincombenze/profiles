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

from fabric.api import *
import StringIO

env.user = 'admin'
env.hosts = ['52.17.173.201']

odoo_instances = [
    'odoo',
]


def deploy():
    with cd('/opt/openerp/profiles/profile_vgstore'):
        sudo('hg pull', user='openerp')
        sudo('hg update', user='openerp')

    restart()


def didotech():
    with cd('/opt/openerp/didotech_80'):
        sudo('hg pull', user='openerp')
        sudo('hg update', user='openerp')


def stop(odoo):
    sudo('service {odoo} stop'.format(odoo=odoo))


def start(odoo):
    sudo('service {odoo} start'.format(odoo=odoo))


def restart_odoo(odoo):
    sudo('service {odoo} restart'.format(odoo=odoo))


def restart(odoo=False):
    """
    $ fab restart:odoo=odoo-gomme
    """
    if odoo:
        restart_odoo(odoo)
    else:
        for odoo in odoo_instances:
            restart_odoo(odoo)


def log(company=False):
    """
    $ fab log:odoo=midaprint
    :param company: il nome della istanza di Odoo
    :return:
    """
    if company:
        run('tail -n 100 /var/log/openerp/odoo-{company}.log'.format(company=company))
    else:
        run('tail -n 100 /var/log/openerp/odoo-server.log')
