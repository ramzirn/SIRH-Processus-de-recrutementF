from odoo import models, fields, api





class Description(models.Model):
    _name = 'sirh.desc'

    recruitment_id = fields.Many2one('sirh.form', string='Recrutement', ondelete='cascade')

    @api.model
    def create(self, vals):
        # Vérifier s'il existe déjà une description pour ce recrutement
        existing_desc = self.search([('recruitment_id', '=', vals.get('recruitment_id'))])
        if existing_desc:
            return existing_desc[0]  # Retourner l'instance existante

        # S'il n'existe pas encore de description, créer une nouvelle instance
        return super(Description, self).create(vals)

    def write(self, vals):
        res = super(Description, self).write(vals)
        # Mettre à jour le formulaire avec l'ID de la description (après création ou modification)
        self.recruitment_id.description_id = self.id if self.recruitment_id else False
        return res

    intitule = fields.Many2one('hr.job', string='Intitulé du poste')
    descr = fields.Text(string='Description du poste', required=True)
    niveau = fields.Selection([
        ('bac', 'Baccalauréat'),
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('doctorat', 'Doctorat'),
    ], string="Niveau d'étude", required=True, default='licence')
    diplome = fields.Selection([('g', 'f')], string="Diplôme")
    formation = fields.Selection([('g', 'f')], string="Formation")
    formation_experience = fields.Selection([('g', 'f')], string="Formation liée à l'expérience du poste")
    savoir_faire = fields.Text(string="Savoir-faire")
    savoir_etre = fields.Text(string="Savoir-être")
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', required=True)
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=False)
    remuneration = fields.Float(string='Rémunération', required=True, default=0)
