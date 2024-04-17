from odoo import models, fields, api


class Evaluation(models.Model):
    _name = 'sirh.evaluation'

    crit = fields.Char(string='Critère')
    observation = fields.Text(string='Observation')
    note = fields.Integer(string='Note/5')
    # savoir_et_connaissance = fields.Integer(string='Savoir et Connaissance', default=0)
    # savoir_faire_et_experience = fields.Integer(string='Savoir-Faire et Expérience', default=0)
    # savoir_etre_et_qualite_requises = fields.Integer(string='Savoir-Être et Qualité Requises', default=0)
    # formations_diplome = fields.Integer(string='Formations et Diplôme', default=0)
    # total_points = fields.Integer(string='Total des Points', compute='_compute_total_points', store=True)


    @api.depends('savoir_et_connaissance', 'savoir_faire_et_experience', 'savoir_etre_et_qualite_requises', 'formations_diplome')
    def _compute_total_points(self):
        for record in self:
            record.total_points = record.savoir_et_connaissance + record.savoir_faire_et_experience + record.savoir_etre_et_qualite_requises + record.formations_diplome

    candidature_id = fields.Many2one('sirh.candidature')
