# -*- coding: utf-8 -*-
from odoo import fields, models
from odoo.exceptions import UserError


class SaleOrderConfirmation(models.Model):
    """ Sale order confirmation wizard model """
    _name = "sale.order.confirmation"

    pick_id = fields.Many2one('stock.picking')

    def action_proceed(self):
        """User accepts the out-of-range transfer quantity."""
        pickings_to_validate_id = self.env.context.get('default_picking_id')
        if pickings_to_validate_id:
            pickings_to_validate = self.env['stock.picking'].browse(pickings_to_validate_id)
            print(pickings_to_validate)
            return pickings_to_validate \
                .with_context(skip_backorder=True, picking_ids_not_to_backorder=self.pick_id.id) \
                .button_validate()
        return True

    def action_back(self):
        """User rejects the transfer and returns to editing."""
        return {'type': 'ir.actions.act_window_close'}
