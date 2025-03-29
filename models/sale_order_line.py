# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderLine(models.Model):
    """ Partner Model """
    _inherit = "sale.order.line"

    tolerance = fields.Integer(string="Tolerance", compute="_compute_tolerance", store=True)

    @api.depends('order_partner_id')
    def _compute_tolerance(self):
        """compute tolerance from partner"""
        for rec in self:
            rec.tolerance = rec.order_partner_id.tolerance

    def _prepare_procurement_values(self, group_id=False):
        res = super()._prepare_procurement_values(group_id)
        res.update({'tolerance': self.tolerance})
        return res
