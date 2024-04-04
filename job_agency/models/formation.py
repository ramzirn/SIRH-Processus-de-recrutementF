from odoo import fields, models


class Formation(models.Model):
    _name = 'sirh.formation'
    _rec_name = 'formation'

    formation = fields.Char(string='Formation', size=100)
