from odoo import models, fields, api
from datetime import datetime, timedelta
import random


class OtpCode(models.TransientModel):
    _name = 'otp.code'
    _description = 'OTP Code'

    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    code = fields.Char(string='OTP Code', required=True)
    expiration = fields.Datetime(string='Expiration', required=True)