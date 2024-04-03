from odoo import models, fields


class Description(models.Model):
    _name = 'sirh.desc'
    _rec_name = 'intitule'

    # recruitment_ida = fields.One2m10any('sirh.form', 'description_ids',string='Recrutement', ondelete='cascade')
    # annonce_ids = fields.Many2one('sirh.annonce', string

    # @api.model
    # def create(self, vals):
    #     # Vérifier s'il existe déjà une description pour ce recrutement
    #     existing_desc = self.search([('recruitment_id', '=', vals.get('recruitment_id'))])
    #     if existing_desc:
    #         return existing_desc[0]  # Retourner l'instance existante
    #
    #     # S'il n'existe pas encore de description, créer une nouvelle instance
    #     return super(Description, self).create(vals)
    #
    # def write(self, vals):
    #     res = super(Description, self).write(vals)
    #     # Mettre à jour le formulaire avec l'ID de la description (après création ou modification)
    #     self.recruitment_id.description_id = self.id if self.recruitment_id else False
    #     return res

    intitule = fields.Many2one('sirh.poste', string='Intitulé du poste')
    descr = fields.Text(string='Description du poste', required=True)
    # Compétences demandées
    niveau = fields.Many2one('hr.recruitment.degree', string="Niveau d'étude", required=True)
    diplome = fields.Many2one('sirh.diplome', string="Diplômes")
    formation = fields.Many2one('sirh.formation', string='Formation')
    formation_experience = fields.Many2one('sirh.formation', string="Formation obligatoire à l’expérience du poste", required=True)
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


class Formation(models.Model):
    _name = 'sirh.formation'
    _rec_name = 'formation'

    formation = fields.Char(string='Formation', size=100)
