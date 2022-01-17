# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Characteristics(models.Model):
    _name = "piradoba.characteristic"
    _description = "Characteristics of identities"

    name = fields.Char(string='Characteristics', size=20, required=True)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            characteristics = self.env['piradoba.characteristic'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if characteristics:
                raise ValidationError('This characteristic already exists!')