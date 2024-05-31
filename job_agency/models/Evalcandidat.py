from odoo import models, fields, api


class CandidateEvaluation(models.Model):
    _name = 'candidate.evaluation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'Candidate Evaluation'

    candidate_name = fields.Many2one('hr.applicant', string='Candidat', required=True)
    interview_date = fields.Date(string="Date d'entretien", required=True)
    position = fields.Many2one('hr.job', string='Poste à pourvoir', required=True)

    tech_competence_points = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Points forts (Compétences techniques)', default='0')
    tech_competence_develop = fields.Text(string='Points à développer (Compétences techniques)')
    tech_competence_note = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Note (1 à 5)', default='0')

    teamwork_capacity = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Capacité de travailler en équipe', default='0')
    adaptation_capacity = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Capacité d\'adaptation', default='0')
    decision_capacity = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Capacité à répondre des décisions', default='0')
    emotion_management = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Capacité à gérer ses émotions', default='0')

    analysis_capacity_points = fields.Text(string='Points forts (Capacité d\'analyse)')
    analysis_capacity_develop = fields.Text(string='Points à développer (Capacité d\'analyse)')
    analysis_capacity_note = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Note (1 à 5)', default='0')

    synthesis_capacity = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Esprit de synthèse', default='0')
    vision_recul = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Vision / Recul', default='0')
    leadership = fields.Selection([
        ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        string='Leadership', default='0')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(CandidateEvaluation, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(CandidateEvaluation, self).write(vals)


class Decison(models.Model):
    _name = 'decision'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    candidate_name = fields.Many2one('hr.applicant', string='Candidat', required=True)
    position = fields.Many2one('hr.job', string='Poste à pourvoir', required=True)

    recruitment_decision = fields.Selection([('yes', 'Oui'), ('no', 'Non')], string='Décision de recrutement', required=True)
    availability_date = fields.Date(string='Date de disponibilité prévisionnelle')
    integration_appointment = fields.Date(string='Rendez-vous pour intégration')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    # @api.depends('recruitment_decision')
    # def _compute_update_readonly(self):
    #     for record in self:
    #         record.availability_date = False
    #         record.integration_appointment = False
    #         if record.recruitment_decision == 'yes':
    #             record.availability_date = True
    #             record.integration_appointment = True

    @api.depends('recruitment_decision')
    def _compute_update_stage(self):
        for record in self:
            if record.candidate_name:
                if record.recruitment_decision == 'yes':
                    record.candidate_name.stage_id = 2  # Stage ID for "Accepted"
                else:
                    record.candidate_name.stage_id = 3  # Stage ID for "Rejected"

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Decision, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Desicion, self).write(vals)
