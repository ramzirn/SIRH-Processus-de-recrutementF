import datetime

from odoo import api, models, fields


class Candidature(models.Model):
    _inherit = ['hr.applicant']

    sexe = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe', track_visibility='onchange',
                            default='female')
    date_naissance = fields.Date(string='Date de Naissance', track_visibility='onchange')
    lieu_naissance = fields.Char("Lieu de Naissance", track_visibility='onchange')
    situation_familiale = fields.Selection([
        ('single', 'Célibataire'),
        ('married', 'Marié(e)'),
        ('divorced', 'Divorcé(e)'),
        ('widowed', 'Veuf/Veuve')],
        "Situation Familiale", track_visibility='onchange')
    adresse = fields.Text(string='Adresse', track_visibility='onchange')
    mobile = fields.Char(string='Mobile', track_visibility='onchange')
    email = fields.Char(string='Email', track_visibility='onchange')
    diplomes = fields.Text(string="Diplômes", track_visibility='onchange')
    specialite = fields.Char(string='Spécialité', size=50, track_visibility='onchange')
    exp_prof = fields.Text(string='Experience professionnelle')
    datedepot = fields.Date(default=datetime.datetime.today(), string="Date depot", track_visibility='onchange')
    deplacement = fields.Char(string='Déplacement', track_visibility='onchange')
    conditionphysique = fields.Selection([
        ('excellente', 'Excellente'),
        ('bonne', 'Bonne'),
        ('moyenne', 'Moyenne'),
        ('faible', 'Faible'),
        ('handicap_leger', 'Handicap léger'),
        ('handicap_important', 'Handicap important'),
        ('apte', 'Apte'),
        ('inapte', 'Inapte')],
        string='Condition Physique', track_visibility='onchange')

    status = fields.Selection([
        ('applied', 'Candidature déposée'),
        ('planned', 'Entretient planifié'),
        ('interviewed', 'Entretient effectué'),
        ('rejected', 'Rejetée'),
        ('approved', 'Approuvée'),
    ], string='État', default='applied')

    totalpt = fields.Integer(string='Total des points', default=0, track_visibility='onchange')
    totalgeneral = fields.Integer(string='Total géneral', default=0, track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.constrains('email', 'mobile')
    def _validate_email_phone(self):
        for record in self:
            if record.email:
                email_regex = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
                if not email_regex.match(record.email):
                    raise ValidationError("Format email invalide.")

            if record.mobile:
                phone_regex = re.compile(r'^[0](5|6|7)[0-9]{8}$')
                if not phone_regex.match(record.mobile):
                    raise ValidationError(
                        "Format numero de telephone invalide.")

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Candidature, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Candidature, self).write(vals)
