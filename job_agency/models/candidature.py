from odoo import models, fields


class Candidature(models.Model):
    _name = 'sirh.candidature'

    candidat_id = fields.Many2one('sirh.candidat', string='Candidat', required=True)
    recrutement_id = fields.Many2one('sirh.form', string='Recrutement', required=True)
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
    docs = fields.One2many('sirh.document', 'doc_id', string='Documents')
    eval = fields.One2many('sirh.evaluation', 'candidature_id')
