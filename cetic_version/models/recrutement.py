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

    intitule = fields.Many2one('hr.job', string='Intitulé du poste', required=True)
    budget = fields.Float(string='Budget', required=True)
    echeanceContrat = fields.Date(string='Échéance du contrat')
    xp = fields.Integer(string='Années d\'expérience', required=True)
    lieu = fields.Char(string='Lieu de travail', required=True)
    Deplacement = fields.Char(string='Déplacement à prévoir')
    autre = fields.Char(string="Autres aspects à considérer")
    dateEntree = fields.Date(string="Date d'entrée")

    desc_id = fields.Many2one('sirh.desc', required=True)
    annonce_id = fields.Many2one('sirh.annonce')

    # def ajout_description(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'sirh.desc',
    #         'view_mode': 'form',
    #         'target': 'new',
    #         'res_id': self.description_id.id,
    #     }

    # def ajout_description(self):
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'res_model': 'sirh.desc',
    #         'view_mode': 'form',
    #         'view_type': 'form',
    #         'view_id': self.env.ref('cetic_version.view_form_description').id,  # Remplacez 'your_module_name'
    #         'target': 'new',
    #         'res_id': self.desc_id.id,
    #     }

    # def show_description(self):
    #     if self.description_id:
    #         return {
    #             'name': 'Description du poste',
    #             'type': 'ir.actions.act_window',
    #             'res_model': 'sirh.desc',
    #             'view_mode': 'form',
    #             'view_type': 'readonly',
    #             'target': 'new',
    #             'res_id': self.description_id.id,
    #         }
    #     else:
    #         return {
    #             'warning': {
    #                 'title': 'Aucune description',
    #                 'message': 'La description n\'est pas disponible pour cet enregistrement.',
    #             }
    #         }

    def ajout_annonce(self):
        return {
            'name': 'Annonce',
            'type': 'ir.actions.act_window',
            'res_model': 'sirh.annonce',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.annonce_ids.id,
        }

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
