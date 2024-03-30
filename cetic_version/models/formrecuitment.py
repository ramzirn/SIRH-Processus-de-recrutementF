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


class FormRecruitment(models.Model):
    _name = 'rh.form'

    description_id = fields.One2many('rh.desc', 'recruitment_id', string='Description', ondelete='cascade')

    @api.model
    def create(self, vals):
        record = super(FormRecruitment, self).create(vals)
        # Automatically create a description record when a form is created
        self.env['rh.desc'].create({'recruitment_id': record.id,
                                    'descr': 'Default Description'
                                    })
        return record

    def unlink(self):
        # When a form is deleted, delete its associated descriptions as well
        self.description_ids.unlink()
        return super(FormRecruitment, self).unlink()

    motif = fields.Selection([
        ('a', 'Recrutement interne'),
        ('b', 'Remplacement temporaire'),
        ('c', 'Retraite'),

        ('a', 'Recrutement interne '),
        ('b', 'remplacement temporaire '),
        ('c', 'retraite '),
    ], string='Motif de recrutement', required=True)

    pourex = fields.Integer(string='Pour l\'exercice', required=True, default=datetime.now().year)

    @api.constrains('pourex')
    def _check_valid_pourex(self):
        for record in self:
            if not est_annee(record.pourex):
                raise ValidationError("Pourex must be an integer between 1900 and 2100")

    budget = fields.Float(required=True)
    intitule = fields.Many2one('hr.job', string='Intitulé du poste', required=True)
    echeanceContrat = fields.Date(string='Échéance du contrat')
    xp = fields.Integer(string='Années d\'expérience', required=True)
    lieu = fields.Char(string='Lieu de travail', required=True)
    Deplacement = fields.Char(string='Déplacement à prévoir')
    autre = fields.Char(string="Autres aspects à considérer")
    dateEntree = fields.Date()

    def fill_description(self):
        # Logique pour ouvrir la vue de description
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'rh.desc',
            'view_mode': 'form',
            'target': 'popup',
            'res_id': self.description_id.id,
        }

    # def show_description(self):
    #     if self.description_id:
    #         return {
    #             'name': 'Description du poste',
    #             'type': 'ir.actions.act_window',
    #             'res_model': 'rh.desc',
    #             'view_mode': 'form',
    #             'target': 'popup',
    #             'res_id': self.description_id.id,
    #         }
    #     else:
    #         return {'warning': 'La description n\'est pas disponible pour cet enregistrement.'}

    def show_description(self):
        if self.description_id:
            return {
                'name': 'Description du poste',
                'type': 'ir.actions.act_window',
                'res_model': 'rh.desc',
                'view_mode': 'form',
                'target': 'popup',
                'res_id': self.description_id.id,
            }
        else:
            return {
                'warning': {
                    'title': 'Aucune description',
                    'message': 'La description n\'est pas disponible pour cet enregistrement.',
                }
            }

    def open_description(self):
        if self.description_id:
            return {
                'name': 'Description du poste',
                'type': 'ir.actions.act_window',
                'res_model': 'rh.desc',
                'view_mode': 'form',
                'target': 'current',
                'res_id': self.description_id.id,
            }
        else:
            return {'warning': 'La description n\'est pas disponible pour cet enregistrement.'}


class Descriptionposte(models.Model):
    _name = 'rh.desc'

    recruitment_id = fields.Many2one('rh.form', string='Recrutement', ondelete='cascade')

    @api.model
    def create(self, vals):
        # Récupérer l'ID du dernier formulaire créé
        last_form = self.env['rh.form'].search([], order='id desc', limit=1)

        # Mettre à jour recruitment_id avec l'ID du dernier formulaire
        vals['recruitment_id'] = last_form.id if last_form else False

        return super(Descriptionposte, self).create(vals)

    def write(self, vals):
        res = super(Descriptionposte, self).write(vals)
        # Mettre à jour le formulaire avec l'ID de la description (après création ou modification)
        self.recruitment_id.description_ids = [(6, 0, [self.id])] if self.recruitment_id else False
        return res

    intitule = fields.Many2one('hr.job', string='Intitulé du poste')
    descr = fields.Text(string='Description du poste', required=True)
    niveau = fields.Selection([
        ('bac', 'Baccalauréat'),
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('doctorat', 'Doctorat'),
    ], string="Niveau d'étude", required=True, default='licence')
    diplome = fields.Selection([('g', 'f')], string="Diplôme")
    formation = fields.Selection([('g', 'f')], string="Formation")
    formation_experience = fields.Selection([('g', 'f')], string="Formation liée à l'expérience du poste")
    savoir_faire = fields.Selection([('g', 'f')], string="Savoir-faire")
    savoir_etre = fields.Selection([('g', 'f')], string="Savoir-être")
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', required=True)
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=False)
    remuneration = fields.Float(string='Rémunération', required=True, default=0)
