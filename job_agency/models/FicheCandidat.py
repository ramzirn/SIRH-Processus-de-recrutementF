from odoo import models, fields, api

class Employee(models.Model):
    _name = 'candidat'

    sexe = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe')
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de Naissance')
    lieu_naissance = fields.Char(string='Lieu de Naissance')
    situation_familiale = fields.Selection(
        [('single', 'Célibataire'), ('married', 'Marié(e)'), ('divorced', 'Divorcé(e)'), ('widowed', 'Veuf/Veuve')],
        string='Situation Familiale')
    adresse = fields.Text(string='Adresse')
    mobile = fields.Char(string='Mobile')
    telephone = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')
    diplome_id = fields.Many2one('hr.recruitment.degree', string='Diplôme')
    specialite = fields.Char(string='Spécialité')

    savoir_et_connaissance = fields.Integer(string='Savoir et Connaissance', default=0)
    savoir_faire_et_experience = fields.Integer(string='Savoir-Faire et Expérience', default=0)
    savoir_etre_et_qualite_requises = fields.Integer(string='Savoir-Être et Qualité Requises', default=0)
    formations_diplome = fields.Integer(string='Formations et Diplôme', default=0)
    total_points = fields.Integer(string='Total des Points', compute='_compute_total_points', store=True)
    observation = fields.Text(string='Observation')

    @api.depends('savoir_et_connaissance', 'savoir_faire_et_experience', 'savoir_etre_et_qualite_requises', 'formations_diplome')
    def _compute_total_points(self):
        for record in self:
            record.total_points = record.savoir_et_connaissance + record.savoir_faire_et_experience + record.savoir_etre_et_qualite_requises + record.formations_diplome
