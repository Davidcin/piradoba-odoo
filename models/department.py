# -*- coding: utf-8 -*-
from odoo import fields, models


class Department(models.Model):
    _name = "piradoba.department"
    _description = "Departments of identities"

    name = fields.Char(string='Department', size=20, required=True)
    employer = fields.One2many("piradoba.identity", "department", string="Employer List")
    manager = fields.Many2one('piradoba.identity', string='Manager')
    _sql_constraints = [
        ('department_name_unique',
         'unique(name)',
         'Department already exists!')
    ]
