from odoo import fields, models, api


class Formation(models.Model):
    _name = 'sirh.formation'
    _rec_name = 'formation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    formation = fields.Char(string='Formation', size=100, track_visibility='onchange')

    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Formation, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Formation, self).write(vals)

