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
    "name": "Alia Account Balance Checks",
    "version": "0.1",
    "author": "Alia Technologies",
    'website': 'http://www.alialabs.com',
    'license': 'AGPL-3',
    "category": "Alia Simple Tools",
    "depends": [
                # Project Dependencies
                'alia_simple_tools_base',
                # Base Dependencies
                'account',
                ],

    "description": """
    This module provide an accounting checks.

    """,
    'data': [
             # Security

             # Reports

             # Views
             'views/alia_account_checks_wizard_view.xml',
             'views/menu_views.xml'
        ],

    'installable': True,
    'active': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: