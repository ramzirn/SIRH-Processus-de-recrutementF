from odoo import models, fields


class Employee(models.Model):
    _name = 'candidat'

    sexe = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe')
    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de Naissance')
    lieu_naissance = fields.Char(string='Lieu de Naissance')
    situation_familiale = fields.Selection(
        [('single', 'Célibataire'), ('married', 'Marié(e)'), ('divorced', 'Divorcé(e)'), ('widowed', 'Veuf/Veuve')],
        string='Situation Familiale')
    adresse = fields.Text(string='Adresse')
    mobile = fields.Char(string='Mobile')
    telephone = fields.Char(string='Téléphone')
    email = fields.Char(string='Email')
    diplome_id = fields.Many2one('hr.recruitment.degree', string='Diplôme')
    specialite = fields.Char(string='Spécialité')

    def name_get(self):
        result = []
        for record in self:
            name = "%s %s" % (record.nom, record.prenom)
            result.append((record.id, name))
        return result
