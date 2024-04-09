from odoo import fields, models


class Document(models.Model):
    _name = 'sirh.document'
    _rec_name = 'name'

    name = fields.Char(string='Nom du document')
    data = fields.Binary(string='Document')
    doc_id = fields.Many2one('sirh.candidature', string='Candidature')
