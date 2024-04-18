from odoo import models, fields, api


class Salle(models.Model):
    _name = 'sirh.salle'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'nom'

    nom = fields.Char(string='Salle', track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Salle, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Salle, self).write(vals)
