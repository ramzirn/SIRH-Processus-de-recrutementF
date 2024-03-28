# from odoo import api, models, fields
# from datetime import datetime
# import re
# from odoo.exceptions import ValidationError
# 
# 
# def est_annee(val):
#     # Vérifier si val est un entier
#     if isinstance(val, int):
#         # Vérifier si val est dans une plage d'années valide
#         if int(datetime.today().year) <= val:  # Par exemple, de 1900 à 2100
#             return True
#     return False
# 
# 
# class FormRecruitment(models.Model):
#     _name = 'rh.formentry'
# 
#     descriptions_ids = fields.One2many('rh.formdesc', 'recruitment_id', string='Descriptions')
#     motif = fields.Selection([
#         ('a', 'Recrutement interne '),
#         ('b', 'remplacement temporaire '),
#         ('c', 'retraite '),
#     ], string='Motif de recrutement', required=True)
# 
#     pourex = fields.Integer(string='Pour lexercice', required=True, default=datetime.now().year)
# 
#     @api.constrains('pourex')
#     def _check_valid_pourex(self):
#         for record in self:
#             if not est_annee(record.pourex):
#                 raise ValidationError("Pourex must be an integer between 1900 and 2100")
# 
#     budget = fields.Float(required=True)
#     intitule = fields.Many2one('hr.job', string='Intitulé du poste', required=True)
#     echeanceContrat = fields.Date(string='Échéance du contrat')
#     xp = fields.Integer(string='Annees dexperience', required=True)
#     lieu = fields.Char(string='Lieu de travail ', required=True)
#     Deplacement = fields.Char(string='deplacement a prévoir')
#     autre = fields.Char(string="Autres aspects a considerer")
#     dateEntree = fields.Date()
# 
#     # @api.model
#     # def create(self, vals):
#     #     recruitment = super(FormRecruitment, self).create(vals)
#     #
#     #     description_id = vals.get('description_id')
#     #
#     #     if description_id:
#     #         recruitment.description_id = description_id
#     #
#     #     return recruitment
# 
#     # @api.multi
#     # def fill_description(self):
#     #     # Ajoutez ici votre logique pour ouvrir la vue de description
#     #     return {
#     #         'type': 'ir.actions.act_window',
#     #         'res_model': 'rh.formdesc',
#     #         'view_mode': 'form',
#     #         'target': 'popup',
#     #         'res_id': self.description_id.id,  # ID de la description liée à cet enregistrement
#     #     }
# 
#     # @api.multi
#     # def show_description(self):
#     #     return {
#     #         'name': 'Description du poste',
#     #         'type': 'ir.actions.act_window',
#     #         'res_model': 'rh.formdesc',
#     #         'view_mode': 'readonly',  # Afficher dans une vue de formulaire
#     #         'target': 'popup',  # Ouvrir dans une nouvelle fenêtre popup
#     #         'res_id': self.description_id.id,  # ID de la description liée à cet enregistrement
#     #     }
# 
#     @api.model
#     def create(self, vals):
#         recruitment = super(FormRecruitment, self).create(vals)
#         # Handle the case when multiple descriptions are passed
#         if 'descriptions_ids' in vals:
#             recruitment.descriptions_ids = vals['descriptions_ids']
#         return recruitment
# 
#     # def fill_description(self):
#     #     # Logic for opening the description view
#     #     return {
#     #         'type': 'ir.actions.act_window',
#     #         'res_model': 'rh.formdesc',
#     #         'view_mode': 'form',
#     #         'target': 'popup',
#     #         'res_id': self.descriptions_ids.id,
#     #     }
#     def fill_description(self):
#         # Logic for opening the description view
#         return {
#             'type': 'ir.actions.act_window',
#             'res_model': 'rh.formdesc',
#             'view_mode': 'form',
#             'target': 'popup',
#             'res_id': self.descriptions_ids.id,
#         }
# 
#     # def show_description(self):
#     #     if self.descriptions_ids:
#     #         return {
#     #             'name': 'Description du poste',
#     #             'type': 'ir.actions.act_window',
#     #             'res_model': 'rh.formdesc',
#     #             'view_mode': 'form',
#     #             'target': 'popup',
#     #             'res_id': self.descriptions_ids.id,
#     #         }
#     #     else:
#     #         return {'warning': 'La description n\'est pas disponible pour cet enregistrement.'}
# 
#     def show_description(self):
#         if self.descriptions_ids:
#             return {
#                 'name': 'Description du poste',
#                 'type': 'ir.actions.act_window',
#                 'res_model': 'rh.formdesc',
#                 'view_mode': 'form',
#                 'target': 'popup',
#                 'res_id': self.descriptions_ids.id,
#             }
#         else:
#             return {'warning': 'La description n\'est pas disponible pour cet enregistrement.'}
# 
# 
# class Descriptionposte(models.Model):
#     _name = 'rh.formdesc'
# 
#     intitule = fields.Many2one('hr.job', string='Intitulé du poste')
# 
#     # @api.model
#     # def default_get(self, fields):
#     #     res = super(Descriptionposte, self).default_get(fields)
#     #     recruitment_id = self.env.context.get('default_recruitment_id')
#     #     if recruitment_id:
#     #         previous_intitule = self.env['rh.formentry'].browse(recruitment_id).intitule.id
#     #         res['intitule'] = previous_intitule
#     #     return res
# 
#     descr = fields.Text(string='Description du poste', required=True)
#     niveau = fields.Selection([
#         ('bac', 'Baccalauréat'),
#         ('licence', 'Licence'),
#         ('master', 'Master'),
#         ('doctorat', 'Doctorat'),
#     ], string="Niveau d'étude", required=True)
#     diplome = fields.Selection([('g', 'f')], string="Diplôme")
#     formation = fields.Selection([('g', 'f')], string="Formation")
#     formation_experience = fields.Selection([('g', 'f')], string="Formation liée à l'expérience du poste")
#     savoir_faire = fields.Selection([('g', 'f')], string="Savoir-faire")
#     savoir_etre = fields.Selection([('g', 'f')], string="Savoir-être")
#     type = fields.Selection([
#         ('CDI', 'CDI'),
#         ('CDD', 'CDD')
#     ], default='CDI', required=True)
#     # temps =
#     horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True)
#     remuneration = fields.Float(string='Remuniration...', required=True),
# 
#     recruitment_id = fields.Many2one('rh.formentry', string='Recrutement')

from odoo import api, models, fields
from datetime import datetime
from odoo.exceptions import ValidationError


<<<<<<< HEAD
def est_annee(val):
    # Vérifier si val est un entier
    if isinstance(val, int):
        # Vérifier si val est dans une plage d'années valide
        if int(datetime.today().year) <= val <= 2100 and val >= 1900:  # Plage d'années valide
            return True
    return False


=======
>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc
class FormRecruitment(models.Model):
    _name = 'rh.formentry'

    descriptions_ids = fields.One2many('rh.formdesc', 'recruitment_id', string='Descriptions')
    motif = fields.Selection([
<<<<<<< HEAD
        ('a', 'Recrutement interne'),
        ('b', 'Remplacement temporaire'),
        ('c', 'Retraite'),
=======
        ('a', 'Recrutement interne '),
        ('b', 'remplacement temporaire '),
        ('c', 'retraite '),
>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc
    ], string='Motif de recrutement', required=True)

    pourex = fields.Integer(string='Pour l\'exercice', required=True, default=datetime.now().year)

    @api.constrains('pourex')
    def _check_valid_pourex(self):
        for record in self:
            if not est_annee(record.pourex):
                raise ValidationError("Pourex must be an integer between 1900 and 2100")

<<<<<<< HEAD
=======
    def est_annee(self, val):
        # Vérifier si val est un entier
        if isinstance(val, int):
            # Vérifier si val est dans une plage d'années valide
            if int(datetime.today().year) <= val:  # Par exemple, de 1900 à 2100
                return True
        return False

>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc
    budget = fields.Float(required=True)
    intitule = fields.Many2one('hr.job', string='Intitulé du poste', required=True)
    echeanceContrat = fields.Date(string='Échéance du contrat')
    xp = fields.Integer(string='Années d\'expérience', required=True)
    lieu = fields.Char(string='Lieu de travail', required=True)
    Deplacement = fields.Char(string='Déplacement à prévoir')
    autre = fields.Char(string="Autres aspects à considérer")
    dateEntree = fields.Date()

    def unlink(self):
        # Supprimer les enregistrements associés dans 'rh.formdesc' avant la suppression dans 'rh.formentry'
        self.descriptions_ids.unlink()
        return super(FormRecruitment, self).unlink()

    def fill_description(self):
        # Logique pour ouvrir la vue de description
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

    @api.model
    def create(self, vals):
        # Créer le formulaire
        form = super(FormRecruitment, self).create(vals)

        # Créer la description liée au formulaire
        description = self.env['rh.formdesc'].create({
            'intitule': form.intitule.id,
            'recruitment_id': form.id,
            # Ajoutez d'autres champs de la description ici
        })

<<<<<<< HEAD
        # Mettre à jour l'ID de la description dans le formulaire
        form.descriptions_ids = [(4, description.id)]
=======
    xp = fields.Float(string='Annees dexperience', required=True)
    lieu = fields.Char(string='Lieu de travail ', required=True)
    Deplacement = fields.Char(string='deplacement a prévoir')
    autre = fields.Char(string="Autres aspects a considerer")
    dateEntree = fields.Date()
>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc

        return form

    def unlink(self):
        for form in self:
            form.descriptions_ids.unlink()
        return super(FormRecruitment, self).unlink()

    def create_description(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'rh.formdesc',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_recruitment_id': self.id}
        }

<<<<<<< HEAD
    def open_description(self):
        if self.descriptions_ids:
            return {
                'name': 'Description du poste',
                'type': 'ir.actions.act_window',
                'res_model': 'rh.formdesc',
                'view_mode': 'form',
                'target': 'current',
                'res_id': self.descriptions_ids.id,
            }
        else:
            return {'warning': 'La description n\'est pas disponible pour cet enregistrement.'}

=======
>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc

class Descriptionposte(models.Model):
    _name = 'rh.formdesc'

<<<<<<< HEAD
    intitule = fields.Many2one('hr.job', string='Intitulé du poste')
    descr = fields.Text(string='Description du poste', required=True)
=======
    intitule = fields.Many2one('rh.formentry', string='Intitulé du poste', required=True)
    descr = fields.Text(String='Description du poste', required=True)
>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc
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
<<<<<<< HEAD
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True)
    remuneration = fields.Float(string='Rémunération', required=True)

    recruitment_id = fields.Many2one('rh.formentry', string='Recrutement')

    @api.model
    def create(self, vals):
        description = super(Descriptionposte, self).create(vals)
        # Mettre à jour l'ID de la description dans le formulaire lié
        if 'recruitment_id' in vals:
            form = self.env['rh.formentry'].browse(vals['recruitment_id'])
            form.descriptions_ids = [(4, description.id)]
        return description
=======
    # temps =
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True)
    remuneration = fields.Float(string='Remuniration...', required=True)
>>>>>>> 685191511935363faf5b529be9df8ce96febfbcc
