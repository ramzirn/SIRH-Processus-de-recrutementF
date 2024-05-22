from odoo import models, fields, api


class Description(models.Model):
    _name = 'sirh.desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'intitule'    ???

    descr = fields.Text(string='Description du poste', required=True, track_visibility='onchange')
    # Compétences demandées
    niveau = fields.Many2one('hr.recruitment.degree', string="Niveau d'étude", required=True, track_visibility='onchange')
    diplome = fields.Text(string='Diplomes', track_visibility='onchange')
    formation = fields.Text(string='Formations', track_visibility='onchange')
    formation_oblig = fields.Text(string="Formation obligatoire à l’expérience du poste", required=True, track_visibility='onchange')
    savoir_faire = fields.Text(string="Savoir-faire", track_visibility='onchange')
    savoir_etre = fields.Text(string="Savoir-être", track_visibility='onchange')
    # Conditions de l’emploi
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDD', string='Type de contrat', required=True, track_visibility='onchange')
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True, track_visibility='onchange')
    remuneration = fields.Float(string='Rémunération', required=True, default=0, track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Description, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Description, self).write(vals)
