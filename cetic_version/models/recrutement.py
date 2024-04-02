from datetime import datetime

from odoo import api, models, fields
from odoo.exceptions import ValidationError


def est_annee(val):
    # Vérifier si val est un entier
    if isinstance(val, int):
        # Vérifier si val est dans une plage d'années valide
        if int(datetime.today().year) <= val <= 2100 and val >= 1900:  # Plage d'années valide
            return True
    return False


class Recrutement(models.Model):
    _name = 'sirh.form'

    description_id = fields.Many2one('sirh.desc', string='Description', ondelete='cascade')
    annonce_id = fields.Many2one('sirh.annonce', string='Annonce', ondelete='cascade')

    # perfect!
    @api.model
    def create(self, vals):
        record = super(Recrutement, self).create(vals)
        if record and not record.description_id:
            # Automatically create a description record when a form is created for the first time
            desc_record = self.env['sirh.desc'].create({
                'intitule': vals.get('intitule', 'Default Intitule'),  # Add other necessary fields
                'descr': 'Default Description',
                'recruitment_id': record.id,
            })
            record.description_id = desc_record.id
            # ////
        if record and not record.annonce_id:
            # Automatically create an annonce record when a form is created for the first time
            annonce_record = self.env['sirh.annonce'].create({
                'contenu': vals.get('contenu', 'Default Contenu'),  # Add other necessary fields
                'recruitment_id': record.id,
            })
            record.annonce_id = annonce_record.id
        return record

    def unlink(self):
        # When a form is deleted, delete its associated descriptions and annonces as well
        self.description_id.unlink()
        # ////
        self.annonce_id.unlink()
        return super(Recrutement, self).unlink()

    motif = fields.Selection([
        ('interne', 'Recrutement interne'),
        ('temp', 'Remplacement temporaire'),
        ('retr', 'Retraite'),
    ], string='Motif de recrutement', required=True)

    pourex = fields.Integer(string='Pour l\'exercice', required=True, default=datetime.now().year)

    @api.constrains('pourex')
    def _check_valid_pourex(self):
        for record in self:
            if not est_annee(record.pourex):
                raise ValidationError("Pourex must be an integer between 1900 and 2100")

    intitule = fields.Many2one('hr.job', string='Intitulé du poste', required=True)
    budget = fields.Float(string='Budget', required=True)
    echeanceContrat = fields.Date(string='Échéance du contrat')
    xp = fields.Integer(string='Années d\'expérience', required=True)
    lieu = fields.Char(string='Lieu de travail', required=True)
    Deplacement = fields.Char(string='Déplacement à prévoir')
    autre = fields.Char(string="Autres aspects à considérer")

    dateEntree = fields.Date(string="Date d'entrée")

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

    def ajout_annonce(self):
        return {
            'name': 'Annonce',
            'type': 'ir.actions.act_window',
            'res_model': 'sirh.annonce',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.annonce_id.id,
        }

    def show_annonce(self):
        if self.annonce_id:
            return {
                'name': 'Détails de l\'annonce',
                'type': 'ir.actions.act_window',
                'res_model': 'sirh.annonce',
                'view_mode': 'form',
                'view_type': 'readonly',
                'target': 'current',
                'res_id': self.annonce_id.id,
            }
        else:
            return {'warning': 'Aucune annonce associée à ce recrutement.'}


