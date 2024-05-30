from odoo import models, fields, api


class Evaluation(models.Model):
    _name = 'sirh.evaluation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    crit = fields.Char(string='Critère', track_visibility='onchange')
    observation = fields.Text(string='Observation', track_visibility='onchange')
    note = fields.Integer(string='Note\n(1 à 5)', track_visibility='onchange')

    applicant_id = fields.Many2one('hr.applicant', string='Applicant', ondelete='cascade', track_visibility='onchange')
    # entretien_id = fields.Many2one('sirh.entretien')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True,
                                 track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True,
                                track_visibility='onchange')

    @api.constrains('note')
    def _check_note_range(self):
        for record in self:
            if not 1 <= record.note <= 5:
                raise ValidationError("La note doit etre entre 1 et 5.")

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Evaluation, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Evaluation, self).write(vals)


