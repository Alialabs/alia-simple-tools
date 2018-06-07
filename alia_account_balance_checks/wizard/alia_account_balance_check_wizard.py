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
from openerp.tools.translate import _
import logging
_logger = logging.getLogger(__name__)




class AliaAccountCheckResult(models.TransientModel):
    """
    This class is used to store comparision results in account balance checks
    """
    _name = 'alia.account.check.result'
    
    account_code = fields.Char("Account code",size=128)
    account_balance_by_account_move_filter = fields.Float("Account Balance by Account Move Filter")
    account_balance_by_account_move_line_filter = fields.Float("Account Balance by Account Move Line Filter")
    account_balance_difference = fields.Float("Account Balance Difference")
    wizard_check_id = fields.Many2one('alia.account.balance.check.wizard')
    



class AliaAccountBalanceCheckWizard(models.TransientModel):
    """
    Main class of wizard
    """
    _name = 'alia.account.balance.check.wizard'
    
    init_date = fields.Date('Init date')
    end_date = fields.Date('End date')
    draft_omit = fields.Boolean('Omit Drafts',default=True)
    special_account_move_omit = fields.Boolean('Omit Special Account Moves (Opening, Closing)',default=True)
    show_accounts_with_differences = fields.Boolean('Show Only Accounts with differences',default=True)
    results = fields.One2many('alia.account.check.result','wizard_check_id')
    
     
    @api.multi
    @api.depends('init_date','end_date','draft_omit','results')
    def check_accounts_balance(self):
        _logger.info("Check Account Balances...")
        model_obj = self.env['ir.model.data']
        data_id = model_obj._get_id('alia_account_balance_checks', 'alia_account_balance_check_results_view')
        view_id = model_obj.browse(data_id).res_id
        
        criteria = []
        results_am = {}
        results_aml = {}
        
        criteria.append(('date','>=',self.init_date))
        criteria.append(('date','<=',self.end_date))
        if self.draft_omit:
            criteria.append(('state','!=','draft'))
        
        if self.special_account_move_omit:
            periods_not_allowed = self.env['account.period'].search([('special','=',True)]).ids
            criteria.append(('period_id','not in',periods_not_allowed))
        
        account_moves = self.env['account.move'].search(criteria)
        account_move_lines = self.env['account.move.line'].search(criteria)
        
        for am in account_moves:
            for aml in am.line_id:
                if str(aml.account_id.code) in results_am.keys():
                    results_am[str(aml.account_id.code)] = results_am[str(aml.account_id.code)] + aml.balance
                else:
                    results_am[str(aml.account_id.code)] = aml.balance
            
        for aml in account_move_lines:
            if str(aml.account_id.code) in results_aml.keys():
                results_aml[str(aml.account_id.code)] = results_aml[str(aml.account_id.code)] + aml.balance
            else:
                results_aml[str(aml.account_id.code)] = aml.balance
        

        balance_check_vals = {}  
        
        items = results_am.items()
        
        for account,balance in items:
            balance_check_vals['account_code'] = account
            balance_check_vals['account_balance_by_account_move_filter'] = balance
            if account in results_aml.keys():
                balance_check_vals['account_balance_by_account_move_line_filter'] = results_aml[str(account)]
                del results_aml[str(account)]
            else:
                balance_check_vals['account_balance_by_account_move_line_filter'] = 0
            
            balance_check_vals['account_balance_difference'] = abs( balance_check_vals['account_balance_by_account_move_filter'] - balance_check_vals['account_balance_by_account_move_line_filter'])  
            
            if self.show_accounts_with_differences:
               if balance_check_vals['account_balance_difference'] == 0:
                   continue                
            self.write({'results':[(0,0,balance_check_vals)]})
        
        return {
            'type':'ir.actions.act_window',
            'name': _('Account Balance Checks'),  
            'res_model':'alia.account.balance.check.wizard',
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
