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

from fabric.api import cd, sudo, get
from fabric.context_managers import env
import datetime

# env.user = 'admin'
# env.hosts = ['52.17.173.201']

env.hosts = [
    'admin@52.17.173.201',  # Production server
]
env.key_filename = '~/.ssh/AmazonProva.pem'


def deploy():
    with cd('/opt/openerp/profiles/profile_enderas'):
        sudo('hg pull', user='openerp')
        sudo('hg update', user='openerp')


def backup(database):
    """
    fab backup:enderas
    """
    # database = 'vampigroup'
    localpath = '/Users/andrei/Programming/lp/backup'
    remotepath = '/opt/backup/{db}/'.format(db=database)
    weekday = datetime.datetime.now().strftime("%A")[:3]

    filename = '{database}_{weekday}.sql.gz'.format(database=database, weekday=weekday)

    get(remotepath + filename, localpath)
