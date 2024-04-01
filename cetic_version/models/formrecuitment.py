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

    description_id = fields.Many2one('rh.desc', string='Description', ondelete='cascade')
    annonce_id = fields.Many2one('annonce', string='Annonce', ondelete='cascade')

    # perfect!
    @api.model
    def create(self, vals):
        record = super(FormRecruitment, self).create(vals)
        if record and not record.description_id:
            # Automatically create a description record when a form is created for the first time
            desc_record = self.env['rh.desc'].create({
                'intitule': vals.get('intitule', 'Default Intitule'),  # Add other necessary fields
                'descr': 'Default Description',
                'recruitment_id': record.id,
            })
            record.description_id = desc_record.id
            # ////
        if record and not record.annonce_id:
            # Automatically create an annonce record when a form is created for the first time
            annonce_record = self.env['annonce'].create({
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
        return super(FormRecruitment, self).unlink()

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
            'res_model': 'rh.desc',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.description_id.id,
        }

    def show_description(self):
        if self.description_id:
            return {
                'name': 'Description du poste',
                'type': 'ir.actions.act_window',
                'res_model': 'rh.desc',
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
            'type': 'ir.actions.act_window',
            'res_model': 'annonce',
            'view_mode': 'form',
            'target': 'new',
            'res_id': self.annonce_id.id,
        }

    def show_annonce(self):
        if self.annonce_id:
            return {
                'name': 'Détails de l\'annonce',
                'type': 'ir.actions.act_window',
                'res_model': 'annonce',
                'view_mode': 'form',
                'view_type': 'readonly',
                'target': 'current',
                'res_id': self.annonce_id.id,
            }
        else:
            return {'warning': 'Aucune annonce associée à ce recrutement.'}


class Descriptionposte(models.Model):
    _name = 'rh.desc'

    recruitment_id = fields.Many2one('rh.form', string='Recrutement', ondelete='cascade')
    @api.model
    def create(self, vals):
        # Vérifier s'il existe déjà une description pour ce recrutement
        existing_desc = self.search([('recruitment_id', '=', vals.get('recruitment_id'))])
        if existing_desc:
            return existing_desc[0]  # Retourner l'instance existante

        # S'il n'existe pas encore de description, créer une nouvelle instance
        return super(Descriptionposte, self).create(vals)

    def write(self, vals):
        res = super(Descriptionposte, self).write(vals)
        # Mettre à jour le formulaire avec l'ID de la description (après création ou modification)
        self.recruitment_id.description_id = self.id if self.recruitment_id else False
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
    savoir_faire = fields.Text(string="Savoir-faire")
    savoir_etre = fields.Text(string="Savoir-être")
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', required=True)
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=False)
    remuneration = fields.Float(string='Rémunération', required=True, default=0)


class Annonce(models.Model):
    _name = 'annonce'

    recruitment_id = fields.Many2one('rh.form', string='Recrutement', ondelete='cascade')

    approche = fields.Selection([
        ('interne', 'Interne'),
        ('externe', 'Externe'),
        ('mixte', 'Mixte')
    ], string='Approche de l\'annonce', default='interne', required=True)

    contenu = fields.Text(string='Contenu de l\'annonce', required=True)
    descriptif_societe = fields.Text(string='Descriptif rapide de la société')
    # description_poste = fields.Text(string='Description du poste')
    profil_recherche = fields.Text(string='Description du profil recherché')
    modalite_reponse = fields.Selection([
        ('a', 'E-mail'),
        ('b', 'Telephone'),
        ('c', 'Autre')
    ], string='Modalités de réponse', default='a', required=True)
    obligations = fields.Text(string='Obligations')
