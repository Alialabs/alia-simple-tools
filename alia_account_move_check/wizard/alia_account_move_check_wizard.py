# -*- coding: utf-8 -*-
####################################
#
#    Created on 17 de septiembre de 2017
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
from openerp.tools.translate import _
import logging
_logger = logging.getLogger(__name__)


class AliaAccountMoveCheckResult(models.TransientModel):
    """
    This class is used to store comparision results in account balance checks
    """
    _name = 'alia.account.move.check.result'
    
    account_move_id = fields.Many2one('account.move',String="Account Move")
    wizard_check_id = fields.Many2one('alia.account.move.check.wizard')
    

class AliaAccountMoveCheckWizard(models.TransientModel):
    """
    Main class of wizard
    """
    _name = 'alia.account.move.check.wizard'
    
    init_date = fields.Date('Init date')
    end_date = fields.Date('End date')
    draft_omit = fields.Boolean('Omit Drafts',default=False)
    special_account_move_omit = fields.Boolean('Omit Special Account Moves (Opening, Closing)',default=True)
    results = fields.One2many('alia.account.move.check.result','wizard_check_id')
       

    @api.multi
    @api.depends('init_date','end_date')
    def _locate_account_move_period(self):
        """
        Description
        """
        account_period_obj = self.env['account.period']
        ids = account_period_obj.search([('date_start','=',self.init_date),('date_stop','=',self.end_date)])
        return ids

        
    @api.multi
    @api.depends('init_date','end_date','draft_omit','special_account_move_omit','results')
    def _get_account_moves(self):
        _logger.info("Get the account moves...")
        criteria = []
        criteria.append(('date','>=',self.init_date))
        criteria.append(('date','<=',self.end_date))
        if self.draft_omit:
            criteria.append(('state','!=','draft'))
        
        if self.special_account_move_omit:
            periods_not_allowed = self.env['account.period'].search([('special','=',True)]).ids
            criteria.append(('period_id','not in',periods_not_allowed))
        
        account_moves = self.env['account.move'].search(criteria)
        return account_moves
    
     
    @api.multi
    @api.depends('init_date','end_date','draft_omit','special_account_move_omit','results')
    def check_account_move_periods(self):
        _logger.info("Check Account Move Periods...")
        model_obj = self.env['ir.model.data']
        data_id = model_obj._get_id('alia_account_move_check', 'alia_account_move_periods_check_view')
        view_id = model_obj.browse(data_id).res_id
        
        account_moves = self._get_account_moves()
        account_error = {}
        for am in account_moves:
            periods = self._locate_account_move_period()
            if am.period_id not in periods:
                account_error['account_move_id'] = am.id
                self.write({'results':[(0,0,account_error)]})
                
        return {
            'type':'ir.actions.act_window',
            'name': _('Account Move Periods Checks'),  
            'res_model':'alia.account.move.check.wizard',
            'view_id':view_id,
            'res_id':self.id,
            'view_mode':'form',
            'view_type':'form',
            'views':[(view_id,'form')],
            'target':'new',
        } 
    
    
    @api.multi
    @api.depends('init_date','end_date')
    def check_account_moves_date_integrity(self):
        _logger.info("Check Account Moves Integrity...")
        pass
    




# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
