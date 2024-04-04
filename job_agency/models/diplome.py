from odoo import fields, models


class Diplome(models.Model):
    _name = 'sirh.diplome'
    _rec_name = 'diplome'

    diplome = fields.Char(string='Formation', size=100)
