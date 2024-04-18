from odoo import models, fields, api


class Description(models.Model):
    _name = 'sirh.desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec_name = 'intitule'    ???

    intitule = fields.Many2one('sirh.poste', string='Intitulé du poste', track_visibility='onchange')
    # afficher le champ lié 'post' de sirh.poste

    descr = fields.Text(string='Description du poste', required=True, track_visibility='onchange')
    # Compétences demandées
    niveau = fields.Many2one('hr.recruitment.degree', string="Niveau d'étude", required=True, track_visibility='onchange')
    diplome = fields.Many2one('sirh.diplome', string="Diplômes", track_visibility='onchange')
    formation = fields.Many2many('sirh.formation', string='Formation', track_visibility='onchange')
    formation_experience = fields.Many2one('sirh.formation', string="Formation obligatoire à l’expérience du poste",
                                           required=True, track_visibility='onchange')
    savoir_faire = fields.Text(string="Savoir-faire", track_visibility='onchange')
    savoir_etre = fields.Text(string="Savoir-être", track_visibility='onchange')
    # Conditions de l’emploi
    type = fields.Selection([
        ('CDI', 'CDI'),
        ('CDD', 'CDD')
    ], default='CDI', string='Type de contrat', required=True, track_visibility='onchange')
    temps = fields.Char(string='Temps de travail', required=True, track_visibility='onchange')
    horaires = fields.Many2one('resource.calendar', string='Horaires de travail', required=True, track_visibility='onchange')
    remuneration = fields.Float(string='Rémunération', required=True, default=0, track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Description, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Description, self).write(vals)
