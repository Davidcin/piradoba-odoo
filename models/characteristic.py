# -*- coding: utf-8 -*-
from odoo import fields, models


class Characteristics(models.Model):
    _name = "piradoba.characteristic"
    _description = "Characteristics of identities"

    name = fields.Char(string='Characteristics', size=20, required=True)

    _sql_constraints = [
        ('characteristic_unique',
         'unique(name)',
         'Characteristic already exists!')
    ]
