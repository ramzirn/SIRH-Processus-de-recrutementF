# from odoo import fields, models, api
# from datetime import datetime
#
#
# class Entretien(models.Model):
#     _name = 'sirh.entretien'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     date_heure = fields.Datetime(string="Date et heure de l'entretien", required=True, track_visibility='onchange', widget='datetime', options={'no_seconds': True})
#     candidat_id = fields.Many2one('sirh.candidat', string='Nom & Prénom du candidat', track_visibility='onchange')
#     candidature_id = fields.Many2one('sirh.candidature', String='Pour la candidature', track_visibility='onchange')
#     responsable = fields.Many2one('hr.employee', track_visibility='onchange',
#                                   domain=lambda self: self._get_responsable_domain())
#     salle = fields.Many2one('sirh.salle', string='Salle', track_visivility='onchange')
#
#     eval = fields.One2many('sirh.evaluationentretien', 'candidature_id', track_visibility='onchange')
#
#     create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
#     write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')
#
#     @api.model
#     def create(self, vals):
#         vals['create_uid'] = self.env.user.id
#         return super(Entretien, self).create(vals)
#
#     @api.multi
#     def write(self, vals):
#         vals['write_uid'] = self.env.user.id
#         return super(Entretien, self).write(vals)
#
#     @api.model
#     def _get_responsable_domain(self):
#         job_responsable_id = self.env['hr.job'].search([('name', '=', 'Responsable de recrutement')], limit=1)
#         return [('job_id', '=', job_responsable_id.id)]
# #