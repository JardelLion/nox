from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_professional = fields.Boolean(string="Is a Professional")
    is_institute = fields.Boolean(string="Is an Institute")
    is_laboratory = fields.Boolean(string="Is a Laboratory")
