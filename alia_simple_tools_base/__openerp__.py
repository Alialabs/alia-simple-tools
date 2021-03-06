# -*- coding: utf-8 -*-
####################################
#
#    Created on 12 de feb. de 2018
#
#    @author:loxo
#
##############################################################################
#
# 2018 ALIA Technologies
#       http://www.alialabs.com
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

{
    "name": "Alia Simple Tools Base",
    "version": "0.1",
    "author": "Alia Technologies",
    'website': 'http://www.alialabs.com',
    'license': 'AGPL-3',
    "category": "Alia Simple Tools",
    "depends": [
                # Project Dependencies
                # Base Dependencies
                'base',
                ],

    "description": """
    This module provide the basis for simple tools.

    """,
    'data': [
             # Security
            'security/alia_simple_tools_base_groups_security.xml',
             # Reports

             # Views
             'views/menu_views.xml'
        ],

    'installable': True,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: