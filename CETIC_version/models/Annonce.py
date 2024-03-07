from odoo import models, fields

class Annonce(models.Model):
    _name = 'annonce'


    approche = fields.Selection([
        ('interne', 'Interne'),
        ('externe', 'Externe'),
        ('mixte', 'Mixte')
    ], string='Approche de l\'annonce', required=True)

    contenu = fields.Text(string='Contenu de l\'annonce', required=True)
    descriptif_societe = fields.Text(string='Descriptif rapide de la société')
    description_poste = fields.Text(string='Description du poste')
    profil_recherche = fields.Text(string='Description du profil recherché')
    modalite_reponse = fields.Selection([
        ('a', 'E-mail'),
        ('b', 'Telephone'),
        ('c', 'Autre')
    ], string='Modalités de réponse', required=True)
    obligations = fields.Text(string='Obligations')
