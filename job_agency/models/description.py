from odoo import models, fields, api


class Description(models.Model):
    _name = 'sirh.desc'
    # _rec_name = 'intitule'    ???

    intitule = fields.Many2one('sirh.poste', string='Intitulé du poste')
    # afficher le champ lié 'post' de sirh.poste

    descr = fields.Text(string='Description du poste', required=True)
    # Compétences demandées
    niveau = fields.Many2one('hr.recruitment.degree', string="Niveau d'étude", required=True)
    diplome = fields.Many2one('sirh.diplome', string="Diplômes")
    formation = fields.Many2many('sirh.formation', string='Formation')
    formation_experience = fields.Many2one('sirh.formation', string="Formation obligatoire à l’expérience du poste",
                                           required=True)
    savoir_faire = fields.Text(string="Savoir-faire")
    savoir_etre = fields.Text(string="Savoir-être")
    # Conditions de l’emploi
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', string='Type de contrat', required=True)
    temps = fields.Char(string='Temps de travail', required=True)
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True)
    remuneration = fields.Float(string='Rémunération', required=True, default=0)
