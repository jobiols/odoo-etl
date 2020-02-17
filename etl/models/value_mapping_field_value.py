#
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class ValueMappingFieldValue(models.Model):
    """"""

    _name = 'etl.value_mapping_field_value'
    _description = 'value_mapping_field_value'

    ext_id = fields.Char(
        string='Key',
        required=True
    )
    name = fields.Char(
        string='Help Name',
        required=True
    )
    value_mapping_field_id = fields.Many2one(
        'etl.value_mapping_field',
        ondelete='cascade',
        string='value_mapping_field_id',
        required=True
    )
