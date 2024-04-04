from odoo import models, fields, api


class Candidat(models.Model):
    _name = 'sirh.candidat'
    _rec_name = 'nom_complet'

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
    email = fields.Char(string='Email')
    diplome = fields.Many2one('sirh.diplome', string="Diplômes")
    specialite = fields.Char(string='Spécialité', size=50)

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
    nom_complet = fields.Char(string='Nom Complet', compute='_compute_nom_complet', store=True)

    @api.depends('nom', 'prenom')
    def _compute_nom_complet(self):
        for candidat in self:
            candidat.nom_complet = f"{candidat.nom} {candidat.prenom}".upper()
