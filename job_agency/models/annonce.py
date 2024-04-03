from odoo import models, fields


class Annonce(models.Model):
    _name = 'sirh.annonce'

    accroche = fields.Selection([
        ('interne', 'Interne'),
        ('externe', 'Externe'),
        ('mixte', 'Mixte')
    ], string='l\'accroche de l\'annonce', default='interne', required=True)
    # contenu de l'annonce
    desc_societe = fields.Text(string='Descriptif rapide de la société', default='CETIC')
    desc_poste = fields.Text(string='Décrire le poste')
    profil_recherche = fields.Text(string='Décrire le profil recherché')
    modalite_reponse = fields.Selection([
        ('email', 'Email'),
        ('tel', 'Telephone'),
        ('fax', 'Fax'),
    ], string='Modalités de réponse', default='email', required=True)
    obligations = fields.Text(string='Les obligations')
