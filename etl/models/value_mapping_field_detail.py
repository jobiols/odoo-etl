#
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class ValueMappingFieldDetail(models.Model):
    """"""

    _name = 'etl.value_mapping_field_detail'
    _description = 'value_mapping_field_detail'

    source_id = fields.Char(
        string='Source ID'
    )
    source_value = fields.Char(

    )
    target_id = fields.Char(
        string='Target ID'
    )
    target_value = fields.Char(

    )
    source_external_model_record_id = fields.Many2one(
        'etl.external_model_record',
        string='Source External Model Record'
    )
    target_external_model_record_id = fields.Many2one(
        'etl.external_model_record',
        string='Target External Model Record'
    )
    source_value_id = fields.Many2one(
        'etl.value_mapping_field_value',
        string='Source Value ID'
    )
    target_value_id = fields.Many2one(
        'etl.value_mapping_field_value',
        string='Target Value ID'
    )
    value_mapping_field_id = fields.Many2one(
        'etl.value_mapping_field',
        ondelete='cascade',
        string='value_mapping_field_id',
        required=True
    )
    source_name = fields.Char(
        related='source_external_model_record_id.name',
        readonly=True,
    )
    source_model_id = fields.Many2one(
        related='value_mapping_field_id.source_model_id',
        relation='etl.external_model',
        string='Source Model',
        readonly=True,
    )
    target_model_id = fields.Many2one(
        related='value_mapping_field_id.target_model_id',
        relation='etl.external_model',
        string='Target Model',
        readonly=True,
    )
