from odoo import models, fields


class GrilleCandidature(models.Model):
    _name = "grillecandidature"

    y = fields.Many2one('candidat', string='Candidat')

    colonne_1 = fields.Char(string="Nom de la colonne 1")
    colonne_2 = fields.Char(string="Nom de la colonne 2")
