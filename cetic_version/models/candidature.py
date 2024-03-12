from odoo import models, fields

class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    candidat_obj = fields.Many2one('candidat', string='Candidat')
    datedepot= fields.Date(required=True)
    conditionphysique=fields.Selection([
        ('a', 'Bonne'),
        ('b', 'Mauvaise'),
        ('c', 'Handicapé'),
    ], string='Condition physique',required=True)

    structure=fields.Selection([
        ('aa', 'A'),
        ('bb', 'B'),
        ('cc', 'C'),
    ], string='Structure',required=True)

    unite=fields.Selection([
        ('aa', 'A'),
        ('bb', 'B'),
        ('cc', 'C'),
    ], string='Unité',required=True)