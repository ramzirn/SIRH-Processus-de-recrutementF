from odoo import fields, models, api


class Document(models.Model):
    _name = 'sirh.document'
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nom du document', track_visibility='onchange')
    data = fields.Binary(string='Document', track_visibility='onchange')
    candidature_id = fields.Many2one('sirh.candidature', string='Candidature', track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Document, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Document, self).write(vals)
