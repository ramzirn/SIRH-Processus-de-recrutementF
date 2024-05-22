from datetime import datetime
from odoo import api, models, fields
from odoo.exceptions import ValidationError


def est_annee(val):
    if isinstance(val, int):
        if int(datetime.today().year) <= val:
            return True
    return False


class Besoin(models.Model):
    _name = 'sirh.besoin'
    _rec_name = 'motif'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    motif = fields.Selection([
        ('interne', 'Recrutement interne'),
        ('temp', 'Remplacement temporaire'),
        ('retr', 'Retraite'),
    ], string='Motif de recrutement', required=True, default='interne', track_visibility='onchange')
    pourex = fields.Integer(string='Pour l\'exercice', required=True, default=datetime.now().year, track_visibility='onchange')
    budget = fields.Float(string='Budget alloué', required=True, track_visibility='onchange')
    intitule = fields.Many2one('sirh.poste', 'Intitulé du poste')
    echeanceContrat = fields.Date(string='Échéance du contrat', track_visibility='onchange')
    # structure =
    xp = fields.Integer(string='Années d\'expérience', required=True, track_visibility='onchange')
    lieu = fields.Char(string='Lieu de travail', required=True, track_visibility='onchange')
    deplacement = fields.Char(string='Déplacement à prévoir', track_visibility='onchange')
    autre = fields.Char(string="Autres aspects à considérer", track_visibility='onchange')
    dateEntree = fields.Date(string="Date d'entrée", track_visibility='onchange')
    domaine_ex = fields.Char(string="Domaine d'experience attendu", track_visibility='onchange')

    desc_id = fields.Many2one('sirh.desc', required=True, string="Rédiger une description", track_visibility='onchange')
    annonce_id = fields.Many2one('sirh.annonce', required=True, string="Rédiger une annonce", track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.constrains('pourex')
    def _check_valid_pourex(self):
        for record in self:
            if not est_annee(record.pourex):
                raise ValidationError("Date d'exercice doit etre superieure a la date d'aujourd'hui.")

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Besoin, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Besoin, self).write(vals)
