# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrder(models.Model):
    """ Partner Model """
    _inherit = "sale.order"

    tolerance = fields.Integer(string="Tolerance", related="partner_id.tolerance")
