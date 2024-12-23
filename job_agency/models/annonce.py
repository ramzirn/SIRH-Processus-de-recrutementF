from odoo import models, fields, api


class Annonce(models.Model):
    _name = 'sirh.annonce'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    accroche = fields.Selection([
        ('Equipe', 'Rejoignez notre équipe'),
        ('Disponibles', 'Postes disponibles'),
        ('Opportunites', 'Opportunités à saisir'),
        ('Talent', 'Devenez notre prochain talent'),
        ('Carriere', 'Carrière chez nous'),
        ('Parcours', 'Enrichissez votre parcours professionnel')
    ], string="L'accroche de l'annonce", default='Equipe', required=True, track_visibility='onchange')
    # contenu de l'annonce
    desc_societe = fields.Text(string='Descriptif rapide de la société', required=True, track_visibility='onchange')
    # poste_id = fields.Many2one('hr.job', "Poste", required=True, track_visibility='onchange')
    desc_poste = fields.Text(string='Description du poste', required=True, track_visibility='onchange')
    profil_recherche = fields.Text(string='Description du profil recherché', required=True, track_visibility='onchange')
    modalite_reponse = fields.Selection([
        ('email', 'Email'),
        ('tel', 'Telephone'),
        ('fax', 'Fax'),
    ], string='Modalités de réponse', default='email', required=True, track_visibility='onchange')
    obligations = fields.Text(string='Obligations', track_visibility='onchange')

    besoin_id = fields.Many2one("sirh.besoin", string="Besoin", required=True)
    # candidature_ids = fields.One2many('sirh.candidature', 'annonce_id')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Annonce, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Annonce, self).write(vals)


