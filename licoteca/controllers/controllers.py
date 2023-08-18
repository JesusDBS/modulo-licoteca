# -*- coding: utf-8 -*-
# from odoo import http


# class Licoteca(http.Controller):
#     @http.route('/licoteca/licoteca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/licoteca/licoteca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('licoteca.listing', {
#             'root': '/licoteca/licoteca',
#             'objects': http.request.env['licoteca.licoteca'].search([]),
#         })

#     @http.route('/licoteca/licoteca/objects/<model("licoteca.licoteca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('licoteca.object', {
#             'object': obj
#         })
