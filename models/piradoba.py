# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Identity(models.Model):
    _name = "piradoba.identity"
    _description = "Identity"

    img = fields.Binary(string="Image", required=True)
    first_name = fields.Char(string='First Name', size=20, required=True)
    last_name = fields.Char(string='Last Name', size=25, required=True)
    citizen = fields.Char(string='Citizenship', size=3, required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='male',
        help="Enter your gender!")
    personal_number = fields.Char(string='Personal Number', size=11, required=True)
    birthday_date = fields.Date(string='Birthday Date', required=True)
    expiry_date = fields.Date(string='Expiry Date', required=True)
    birth_place = fields.Char(string='Birth Place', size=20, required=True)
    issue_date = fields.Date(string='Issue Date', required=True)
    department = fields.Many2one('piradoba.department', string= 'Department', required=True)
    characteristic = fields.Many2many('piradoba.characteristic', string= 'Characteristics', required=True)

    @api.constrains("personal_number")
    def unique(self):
        for rec in self:
            personalnum = self.env['piradoba.identity'].search([('personal_number', '=', rec.personal_number), ('id', '!=', rec.id)])
            if personalnum:
                raise ValidationError('This personal number already exists!')

    @api.constrains("personal_number")
    def numeric(self):
        for rec in self:
            if rec.personal_number.isnumeric() == False:
                raise ValidationError('Wrong datatype is used in Personal number field!')

    @api.constrains("personal_number")
    def num_length(self):
        for rec in self:
            if len(rec.personal_number) != 11:
                raise ValidationError('Personal number requires 11 numbers!')

    @api.constrains("citizen")
    def uppercit(self):
        for rec in self:
            for letter in rec.citizen:
                if letter.islower():
                    raise ValidationError('In citizenship every letter must be uppercase!')

    @api.constrains("first_name")
    def fnamealpha(self):
        for rec in self:
            if rec.first_name[0].islower():
                    raise ValidationError('First letter of name must be uppercase!')

    @api.constrains("last_name")
    def lnamealpha(self):
        for rec in self:
            if rec.last_name[0].islower():
                    raise ValidationError('First letter of last name must be uppercase!')

    @api.constrains("last_name")
    def cityalpha(self):
        for rec in self:
            if rec.birth_place[0].islower():
                raise ValidationError('First letter of birth place must be uppercase!')

    @api.constrains('birthday_date')
    def check_date_b(self):
        for rec in self:
            if rec.birthday_date > fields.Date.today():
                raise ValidationError('Birthday cannot be in the future!')

    @api.constrains('expiry_date')
    def check_date_i(self):
        for rec in self:
            if rec.issue_date > fields.Date.today():
                raise ValidationError('Issue date cannot be in the future!')