from odoo import models, fields


class Candidature(models.Model):
    _name = 'sirh.candidature'

    candidat_id = fields.Many2one('sirh.candidat', string='Candidat', required=True)

    datedepot = fields.Date(required=True)
    disponibilite = fields.Boolean(string="Disponibilité")
    conditionphysique = fields.Selection([
        ('excellente', 'Excellente'),
        ('bonne', 'Bonne'),
        ('moyenne', 'Moyenne'),
        ('faible', 'Faible'),
        ('handicap_leger', 'Handicap léger'),
        ('handicap_important', 'Handicap important'),
        ('apte', 'Apte'),
        ('inapte', 'Inapte')],
        string='Condition Physique')
    departement = fields.Many2one('hr.department')
    # structure =
    # unite =
    # cv = fields.Binary(string='CV')
    docs = fields.Many2many('sirh.document', '', string='Documents')

