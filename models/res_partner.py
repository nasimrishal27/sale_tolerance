# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    """ Partner Model """
    _inherit = "res.partner"

    tolerance = fields.Integer(string="Sale Tolerance", default=0)