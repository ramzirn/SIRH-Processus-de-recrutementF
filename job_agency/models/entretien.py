from odoo import fields, models
from datetime import datetime


class Entretien(models.Model):
    _name = 'sirh.entretien'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    date_heure = fields.Datetime(string="Date et heure de début", required=True)
