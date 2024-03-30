from odoo import api, models, fields
from datetime import datetime
from odoo.exceptions import ValidationError


def est_annee(val):
    if isinstance(val, int):
        if int(datetime.today().year) <= val <= 2100 and val >= 1900:
            return True
    return False


class FormRecruitment(models.Model):
    _name = 'rh.formentry'

    descriptions_ids = fields.One2many('rh.formdesc', 'recruitment_id', string='Descriptions')
    motif = fields.Selection([
        ('a', 'Recrutement interne'),
        ('b', 'Remplacement temporaire'),
        ('c', 'Retraite'),
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

    @api.model
    def create(self, vals):
        form = super(FormRecruitment, self).create(vals)
        description = self.env['rh.formdesc'].create({
            'intitule': form.intitule.id,
            'recruitment_id': form.id,
        })
        form.descriptions_ids = [(4, description.id)]
        return form

    def fill_description(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'rh.formdesc',
            'view_mode': 'form',
            'target': 'popup',
            'res_id': self.descriptions_ids.id,
        }

    def show_description(self):
        if self.descriptions_ids:
            return {
                'name': 'Description du poste',
                'type': 'ir.actions.act_window',
                'res_model': 'rh.formdesc',
                'view_mode': 'form',
                'target': 'popup',
                'res_id': self.descriptions_ids.id,
            }
        else:
            return {'warning': 'La description n\'est pas disponible pour cet enregistrement.'}


class Descriptionposte(models.Model):
    _name = 'rh.formdesc'

    intitule = fields.Many2one('hr.job', string='Intitulé du poste', required=True)
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
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True)
    remuneration = fields.Float(string='Rémunération', required=True)
    recruitment_id = fields.Many2one('rh.formentry', string='Recrutement')

    @api.model
    def create(self, vals):
        description = super(Descriptionposte, self).create(vals)
        if 'recruitment_id' in vals:
            form = self.env['rh.formentry'].browse(vals['recruitment_id'])
            form.descriptions_ids = [(4, description.id)]
        return description
