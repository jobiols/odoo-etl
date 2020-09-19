#
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class ExternalModelRecord(models.Model):
    _name = 'etl.external_model_record'
    _description = 'external_model_record'

    ext_id = fields.Char(
        string='Value To be Mapped',
        required=True
    )
    name = fields.Char(
        string='Help Name',
        required=True
    )
    external_model_id = fields.Many2one(
        'etl.external_model',
        ondelete='cascade',
        string='external_model_id',
        required=True
    )
