# -*- coding: utf-8 -*-
####################################
#
#    Created on  de septiembre de 2017
#
#    @author: Cástor
#
##############################################################################
#
# 2016 ALIA Technologies
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


from openerp import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)


class productPricelist(models.Model): 
    _inherit = 'product.pricelist' 

    amount_assigns = fields.Integer(compute='_get_amount_assigns')

    @api.one
    @api.depends('amount_assigns')
    def _get_amount_assigns(self):
        self.amount_assigns = len(self.env['ir.property'].search([('name','=','property_product_pricelist'),('value_reference','=',str('product.pricelist')+','+str(self.id)),('res_id','like','res.partner')]))
        




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
