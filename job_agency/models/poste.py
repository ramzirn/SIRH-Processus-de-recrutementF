from odoo import fields, models, api


class PosteTra(models.Model):
    # _name = 'sirh.poste'
    _inherit = ['hr.job', 'mail.activity.mixin']

    besoin_ids = fields.One2many("sirh.besoin", "intitule", string="Besoins")

    # details du poste
    create_uid = fields.Many2one('res.users', string='Created by', readonly=True, track_visibility='onchange')
    write_uid = fields.Many2one('res.users', string='Last Updated by', readonly=True, track_visibility='onchange')

    @api.model
    def create(self, vals):
        vals['create_uid'] = self.env.user.id
        return super(Job, self).create(vals)

    @api.multi
    def write(self, vals):
        vals['write_uid'] = self.env.user.id
        return super(Job, self).write(vals)

