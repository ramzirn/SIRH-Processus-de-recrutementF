import datetime

from odoo import models, fields, api


class Candidature(models.Model):
    _name = 'sirh.candidature'
    _rec_name = 'nom_complet'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sexe = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe', track_visibility='onchange')
    nom = fields.Char(string='Nom', required=True, track_visibility='onchange')
    prenom = fields.Char(string='Prénom', required=True, track_visibility='onchange')
    date_naissance = fields.Date(string='Date de Naissance', track_visibility='onchange')
    lieu_naissance = fields.Char(string='Lieu de Naissance', track_visibility='onchange')
    situation_familiale = fields.Selection([
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve')],
        string='Situation Familiale', track_visibility='onchange')
    adresse = fields.Text(string='Adresse', track_visibility='onchange')
    mobile = fields.Char(string='Mobile', track_visibility='onchange')
    email = fields.Char(string='Email', track_visibility='onchange')
    niveau = fields.Many2one('hr.recruitment.degree', string="Niveau d'étude", track_visibility='onchange')
    diplomes = fields.Text(string="Diplômes", track_visibility='onchange')
    specialite = fields.Char(string='Spécialité', size=50, track_visibility='onchange')

    exp_prof = fields.Text(string='Experience professionnelle')
    # date depot automatiquement rempli
    datedepot = fields.Date(default=datetime.datetime.today(), string="Date depot", track_visibility='onchange')
    disponibilite = fields.Text(string="Disponibilité", track_visibility='onchange')
    salaire_dem = fields.Float(string="Salaire demandé", track_visibility='onchange')
    deplacement = fields.Char(string='Déplacement', track_visibility='onchange')
    conditionphysique = fields.Selection([
        ('excellente', 'Excellente'),
        ('bonne', 'Bonne'),
        ('moyenne', 'Moyenne'),
        ('faible', 'Faible'),
        ('handicap_leger', 'Handicap léger'),
        ('handicap_important', 'Handicap important'),
        ('apte', 'Apte'),
        ('inapte', 'Inapte')],
        string='Condition Physique', track_visibility='onchange')
    docs = fields.One2many('sirh.document', 'doc_id', string='Documents', track_visibility='onchange')

    status = fields.Selection([
        ('applied', 'Candidature déposée'),
        ('planned', 'Entretient planifié'),
        ('interviewed', 'Entretient effectué'),
        ('rejected', 'Rejetée'),
        ('approved', 'Approuvée'),
    ], string='État', default='applied')

    totalpt = fields.Integer(string='Total des points', default=0, track_visibility='onchange')
    totalgeneral = fields.Integer(string='Total géneral', default = 0, track_visibility='onchange')

    annonce_id = fields.Many2one('sirh.annonce', string='Annonce', required=True, track_visibility='onchange')
    eval = fields.One2many('sirh.evaluation', 'candidature_id', track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    nom_complet = fields.Char(string='Nom Complet', compute='_compute_nom_complet', store=True)

    @api.depends('nom', 'prenom')
    def _compute_nom_complet(self):
        for candidat in self:
            candidat.nom_complet = f"{candidat.nom} {candidat.prenom}".upper()

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Candidature, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Candidature, self).write(vals)
