# -*- coding: utf-8 -*-
from odoo import _, api, fields, models


class StockPicking(models.Model):
    """ Partner Model """
    _inherit = "stock.picking"

    hide_validate_button = fields.Boolean(compute="_compute_hide_validate_button", store=True)

    @api.depends('move_ids.quantity', "move_ids_without_package")
    def _compute_hide_validate_button(self):
        for picking in self:
            if picking.move_ids.filtered(lambda l: l.quantity < 5 or l.quantity > 15):
                picking.hide_validate_button = True
            else:
                picking.hide_validate_button = False

    def action_validate(self):
        """"""
        view = self.env.ref('sale_tolerance.view_sale_order_confirmation')
        return {
            'name': _('Sale Order Confirmation'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'sale.order.confirmation',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'context': {
                'default_picking_id': self.id,
            }
        }
