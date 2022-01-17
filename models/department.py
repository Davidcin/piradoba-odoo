# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Department(models.Model):
    _name = "piradoba.department"
    _description = "Departments of identities"

    name = fields.Char(string='Department',size=20, required=True)

    @api.constrains('name')
    def check_name(self):
        for rec in self:
            departments = self.env['piradoba.department'].search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if departments:
                raise ValidationError('This department already exists!')