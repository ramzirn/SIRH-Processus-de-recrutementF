from datetime import datetime

from odoo import api, models, fields
from odoo.exceptions import ValidationError


def est_annee(val):
    if isinstance(val, int):
        if int(datetime.today().year) <= val:
            return True
    return False


class Recrutement(models.Model):
    _name = 'sirh.form'
    _rec_name = 'motif'

    motif = fields.Selection([
        ('interne', 'Recrutement interne'),
        ('temp', 'Remplacement temporaire'),
        ('retr', 'Retraite'),
    ], string='Motif de recrutement', required=True, default='interne')
    pourex = fields.Integer(string='Pour l\'exercice', required=True, default=datetime.now().year)

    @api.constrains('pourex')
    def _check_valid_pourex(self):
        for record in self:
            if not est_annee(record.pourex):
                raise ValidationError("Date d'exercice doit etre superieure a la date d'aujourd'hui.")

    budget = fields.Float(string='Budget alloué', required=True)
    intitule = fields.Many2one('sirh.poste', string='Intitulé du poste', required=True)
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', string='Nature du contrat', required=True)
    echeanceContrat = fields.Date(string='Échéance du contrat', required=True)
    stru = fields.Many2one('hr.department', string='Structure concernée', required=True)
    xp = fields.Integer(string='Nombre d\'années d\'expérience', required=True)
    lieu = fields.Char(string='Lieu de travail', required=True)
    deplacement = fields.Char(string='Déplacement à prévoir', required=True)
    autre = fields.Char(string="Autres aspects à considérer")

    def ajout_description(self):

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'sirh.desc',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.description_id.id,
        }

    def show_description(self):
        if self.description_id:
            return {
                'name': 'Description du poste',
                'type': 'ir.actions.act_window',
                'res_model': 'sirh.desc',
                'view_mode': 'form',
                'view_type': 'readonly',
                'target': 'new',
                'res_id': self.description_id.id,
            }
        else:
            return {
                'warning': {
                    'title': 'Aucune description',
                    'message': 'La description n\'est pas disponible pour cet enregistrement.',
                }
            }

    desc_id = fields.Many2one('sirh.desc', required=True)
    annonce_id = fields.Many2one('sirh.annonce')
    dateEntree = fields.Date(string="Date d'entrée souhaitée", required=True)
    dom = fields.Many2one('sirh.domainexp', string="Domaine(s) d'experience(s) attendu(s)", required=True)


class DomaineExp(models.Model):
    _name = 'sirh.domainexp'
    _rec_name = 'dom'

    dom = fields.Char(string="Domaine(s) d'experience(s) attendu(s)", size=50)


class Poste(models.Model):
    _name = 'sirh.poste'
    _rec_name = 'post'

    def show_annonce(self):
        if self.annonce_id:
            return {
                'type': 'ir.actions.act_window',
                'res_model': 'sirh.annonce',
                'view_mode': 'form',
                'view_type': 'readonly',
                'target': 'current',
                'res_id': self.annonce_id.id,
            }
        else:
            return {'warning': 'Aucune annonce associée à ce recrutement.'}

    def show_description(self):
        a = self.env['sirh.desc'].search([('id', '=', self.desc_id.id)])

    post = fields.Char(string="Intitulé du poste", size=50)
