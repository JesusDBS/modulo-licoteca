# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Drink(models.Model):
    _name = 'licoteca.drink'
    _description = 'Alcoholic Drinks'

    TYPE = [
        ('fermentada', 'Fermentada'),
        ('destilada', 'Destilada')
    ]

    name = fields.Char(string="Bebida", require=True)
    alcohol_degree = fields.Float(string="Grado Etilico")
    type = fields.Selection(TYPE, string="Tipo de beida alcoholica", default='fermentada')

