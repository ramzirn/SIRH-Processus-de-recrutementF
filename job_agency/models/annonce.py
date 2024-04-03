from odoo import models, fields


class Annonce(models.Model):
    _name = 'sirh.annonce'

    approche = fields.Selection([
        ('interne', 'Interne'),
        ('externe', 'Externe'),
        ('mixte', 'Mixte')
    ], string='Approche de l\'annonce', default='interne', required=True)
    contenu = fields.Text(string='Contenu de l\'annonce', required=True)
    descriptif_societe = fields.Text(string='Descriptif rapide de la société', default='CETIC')
    # description_poste = fields.Text(string='Description du poste')
    profil_recherche = fields.Text(string='Description du profil recherché')
    modalite_reponse = fields.Selection([
        ('a', 'E-mail'),
        ('b', 'Telephone'),
    ], string='Modalités de réponse', default='a', required=True)
    obligations = fields.Text(string='Obligations')
