from odoo import models, fields


class CandidateEvaluation(models.Model):
    _name = 'candidate.evaluation'
    _description = 'Candidate Evaluation'

    candidate_name = fields.Many2one('hr.applicant', string='Candidat')

    interview_date = fields.Date(string="Date d'entretien")
    position = fields.Char(string='Poste à pourvoir')

    tech_competence_points = fields.Integer(string='Points forts (Compétences techniques)')
    tech_competence_develop = fields.Text(string='Points à développer (Compétences techniques)')
    tech_competence_note = fields.Selection([(str(num), str(num)) for num in range(1, 6)], string='Note (1 à 5)')

    teamwork_capacity = fields.Integer(string='Capacité de travailler en équipe')
    adaptation_capacity = fields.Integer(string='Capacité d\'adaptation')
    decision_capacity = fields.Integer(string='Capacité à répondre des décisions')
    emotion_management = fields.Integer(string='Capacité à gérer ses émotions')

    analysis_capacity_points = fields.Text(string='Points forts (Capacité d\'analyse)')
    analysis_capacity_develop = fields.Text(string='Points à développer (Capacité d\'analyse)')
    analysis_capacity_note = fields.Selection([(str(num), str(num)) for num in range(1, 6)], string='Note (1 à 5)')

    synthesis_capacity = fields.Integer(string='Esprit de synthèse')
    vision_recul = fields.Integer(string='Vision / Recul')
    leadership = fields.Integer(string='Leadership')

    recruitment_decision = fields.Selection([('yes', 'Oui'), ('no', 'Non')], string='Décision de recrutement')
    availability_date = fields.Date(string='Date de disponibilité prévisionnelle')
    integration_appointment = fields.Date(string='RDV pour intégration')