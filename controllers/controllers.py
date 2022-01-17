# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Piradoba(http.Controller):
    @http.route('/piradoba/json', type='json', auth='user')
    def json(self, **post):
        identity_rec = request.env['piradoba.identity'].search([])
        identities = []
        for rec in identity_rec:
            vals = {
                'first_name': rec.first_name,
                'last_name': rec.last_name,
                'citizen': rec.citizen,
                'gender': rec.gender,
                'personal_number': rec.personal_number,
                'birthday_date': rec.birthday_date,
                'expiry_date': rec.expiry_date,
                'birth_place': rec.birth_place,
                'issue_date': rec.issue_date,
                'department': rec.department,
                'characteristic': rec.characteristic
            }
            identities.append(vals)
        data = {'status': 200, 'response': identities, 'message': 'Success'}
        return data

#     @http.route('/piradoba/piradoba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('piradoba.listing', {
#             'root': '/piradoba/piradoba',
#             'objects': http.request.env['piradoba.piradoba'].search([]),
#         })

#     @http.route('/piradoba/piradoba/objects/<model("piradoba.piradoba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('piradoba.object', {
#             'object': obj
#         })
