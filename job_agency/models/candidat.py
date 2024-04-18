from odoo import models, fields, api


class Candidat(models.Model):
    _name = 'sirh.candidat'
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
    diplomes = fields.Many2many('sirh.diplome', string="Diplômes", track_visibility='onchange')
    specialite = fields.Char(string='Spécialité', size=50, track_visibility='onchange')

    nom_complet = fields.Char(string='Nom Complet', compute='_compute_nom_complet', store=True)

    @api.depends('nom', 'prenom')
    def _compute_nom_complet(self):
        for candidat in self:
            candidat.nom_complet = f"{candidat.nom} {candidat.prenom}".upper()

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Candidat, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Candidat, self).write(vals)
