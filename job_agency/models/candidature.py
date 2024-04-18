from odoo import models, fields, api


class Candidature(models.Model):
    _name = 'sirh.candidature'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    candidat_id = fields.Many2one('sirh.candidat', string='Candidat', required=True, track_visibility='onchange')
    recrutement_id = fields.Many2one('sirh.form', string='Recrutement', required=True, track_visibility='onchange')
    datedepot = fields.Date(required=True, string="Date depot", track_visibility='onchange')
    disponibilite = fields.Boolean(string="Disponibilité", track_visibility='onchange')
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
    departement = fields.Many2one('hr.department', track_visibility='onchange')
    # structure =
    # unite =
    docs = fields.One2many('sirh.document', 'doc_id', string='Documents', track_visibility='onchange')
    eval = fields.One2many('sirh.evaluation', 'candidature_id', track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Candidature, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Candidature, self).write(vals)
