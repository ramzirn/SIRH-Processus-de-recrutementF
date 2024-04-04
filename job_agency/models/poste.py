from odoo import fields, models


class Poste(models.Model):
    _name = 'sirh.poste'
    _rec_name = 'post'

    post = fields.Char(string="Intitulé du poste", size=50)
