from odoo import api, models, fields
from datetime import datetime
import re
from odoo.exceptions import ValidationError

class FormRecruitment(models.Model):
    _name = 'rh.formentry'

    motif = fields.Selection([
        ('a', 'Recrutement interne '),
        ('b', 'remplacement temporaire '),
        ('c', 'retraite '),
    ], string='Motif de recrutement',required=True)

    pourex = fields.Integer(string='Pour lexercice', required=True, default=datetime.now().year)

    @api.constrains('pourex')
    def _check_valid_pourex(self):
        for record in self:
            if not self.est_annee(record.pourex):
                raise ValidationError("Pourex must be an integer between 1900 and 2100")

    def est_annee(self, val):
        # Vérifier si val est un entier
        if isinstance(val, int):
            # Vérifier si val est dans une plage d'années valide
            if int(datetime.today().year) <= val:  # Par exemple, de 1900 à 2100
                return True
        return False

    budget=fields.Float(required=True)
    intitule=fields.Many2one('hr.job', string='Intitulé du poste', required=True)
    echeanceContrat = fields.Date(string='Échéance du contrat')
    xp=fields.Integer(string='Annees dexperience',required=True)
    lieu=fields.Char(string='Lieu de travail ', required=True)
    Deplacement=fields.Char(string='deplacement a prévoir')
    autre=fields.Char(string="Autres aspects a considerer")
    dateEntree=fields.Date()

    # description_id = fields.Many2one('rh.formdesc', string='Description du poste')
    description_id = fields.One2many('rh.formentry')

    @api.model
    def create(self, vals):
        recruitment = super(FormRecruitment, self).create(vals)

        description_id = vals.get('description_id')

        if description_id:
            recruitment.description_id = description_id

        return recruitment

    @api.multi
    def fill_description(self):
        # Ajoutez ici votre logique pour ouvrir la vue de description
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'rh.formdesc',
            'view_mode': 'form',
            'target': 'popup',
            'res_id': self.description_id.id,  # ID de la description liée à cet enregistrement
        }

    @api.multi
    def show_description(self):
        return {
            'name': 'Description du poste',
            'type': 'ir.actions.act_window',
            'res_model': 'rh.formdesc',
            'view_mode': 'readonly',  # Afficher dans une vue de formulaire
            'target': 'popup',  # Ouvrir dans une nouvelle fenêtre popup
            'res_id': self.description_id.id,  # ID de la description liée à cet enregistrement
        }

class Descriptionposte(models.Model):
    _name = 'rh.formdesc'

    intitule = fields.Many2one('hr.job', string='Intitulé du poste')
    recruitment_id = fields.Many2one('rh.formentry', string='Recrutement')

    @api.model
    def default_get(self, fields):
        res = super(Descriptionposte, self).default_get(fields)
        recruitment_id = self.env.context.get('default_recruitment_id')
        if recruitment_id:
            previous_intitule = self.env['rh.formentry'].browse(recruitment_id).intitule.id
            res['intitule'] = previous_intitule
        return res

    descr = fields.Text(string='Description du poste', required=True)
    niveau = fields.Selection([
        ('bac', 'Baccalauréat'),
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('doctorat', 'Doctorat'),
    ], string="Niveau d'étude", required=True)
    diplome = fields.Selection([('g', 'f')], string="Diplôme")
    formation = fields.Selection([('g', 'f')], string="Formation")
    formation_experience = fields.Selection([('g', 'f')], string="Formation liée à l'expérience du poste")
    savoir_faire = fields.Selection([('g', 'f')], string="Savoir-faire")
    savoir_etre = fields.Selection([('g', 'f')], string="Savoir-être")
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', required=True)
    # temps =
    horaires = fields.Many2one('resource.calendar' , string='Horaires de travail', required=True)
    remuneration = fields.Float(string='Remuniration...' ,required=True)