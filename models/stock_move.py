# -*- coding: utf-8 -*-
from odoo import fields, models


class StockMove(models.Model):
    """ Partner Model """
    _inherit = "stock.move"

    tolerance = fields.Integer(string="Tolerance")

class StockRule(models.Model):
    """ Stock rule model """
    _inherit = 'stock.rule'

    def _get_custom_move_fields(self):
        fields = super()._get_custom_move_fields()
        fields += ['tolerance']
        return fields
