from odoo import fields, models, api
from datetime import datetime


class Entretien(models.Model):
    _name = 'sirh.entretien'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # candidature_id = fields.Many2one('sirh.candidature', string='Nom & Prénom du candidat', required=True, track_visibility='onchange')
    date_heure = fields.Datetime(string="Date et heure de l'entretien", required=True, track_visibility='onchange')
    # le responsable est le recruteur
    responsable = fields.Many2one('hr.employee', track_visibility='onchange', domain=lambda self: self._get_recruteur_domain())
    # l'interim est le  gestionnaire RH
    interim = fields.Many2one('hr.employee', track_visibility='onchange', domain=lambda self: self._get_gestionnairerh_domain())
    salle = fields.Text(string='Salle', track_visivility='onchange')

    totalpt = fields.Integer(string='Total des points', default = 0, track_visibility='onchange')

    # eval_id = fields.One2many('sirh.evaluation', 'entretien_id', track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Entretien, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Entretien, self).write(vals)

    @api.model
    def _get_recruteur_domain(self):
        job_responsable_id = self.env['hr.job'].search([('name', '=', 'Responsable de recrutement')], limit=1)
        return [('job_id', '=', job_responsable_id.id)]

    @api.model
    def _get_gestionnairerh_domain(self):
        # job_responsable_id = self.env['hr.job'].search([('name', '=', 'Responsable de recrutement')], limit=1)
        # return [('job_id', '=', job_responsable_id.id)]
        pass
