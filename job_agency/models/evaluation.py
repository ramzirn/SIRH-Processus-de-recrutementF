from odoo import models, fields, api


class Evaluation(models.Model):
    _name = 'sirh.evaluation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    crit = fields.Char(string='Critère', track_visibility='onchange')
    observation = fields.Text(string='Observation', track_visibility='onchange')
    note = fields.Integer(string='Note\n(1 à 5)', track_visibility='onchange')

    # candidature_id = fields.Many2one('sirh.candidature')
    entretien_id = fields.Many2one('sirh.entretien')
    @api.constrains('note')
    def _check_note_range(self):
        for record in self:
            if not 1 <= record.note <= 5:
                raise ValidationError("La note doit etre entre 1 et 5.")

    candidature_id = fields.Many2one('sirh.candidature')
    entretien_id = fields.Many2one('sirh.entretien')

    # savoir_et_connaissance = fields.Integer(string='Savoir et Connaissance', default=0)
    # savoir_faire_et_experience = fields.Integer(string='Savoir-Faire et Expérience', default=0)
    # savoir_etre_et_qualite_requises = fields.Integer(string='Savoir-Être et Qualité Requises', default=0)
    # formations_diplome = fields.Integer(string='Formations et Diplôme', default=0)
    # total_points = fields.Integer(string='Total des Points', compute='_compute_total_points', store=True)

    # @api.depends('savoir_et_connaissance', 'savoir_faire_et_experience', 'savoir_etre_et_qualite_requises',
    #              'formations_diplome')
    # def _compute_total_points(self):
    #     for record in self:
    #         record.total_points = (record.savoir_et_connaissance + record.savoir_faire_et_experience +
    #                                record.savoir_etre_et_qualite_requises + record.formations_diplome)

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Evaluation, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Evaluation, self).write(vals)
