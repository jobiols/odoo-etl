#
##############################################################################
# For copyright and license notices, see __manifest_.py file in module root
# directory
##############################################################################
from odoo import models, fields


class ValueMappingField(models.Model):
    _name = 'etl.value_mapping_field'
    _description = 'value_mapping_field'

    name = fields.Char(
        string='Field Name',
        required=True
    )
    type = fields.Selection(
        [(u'id', u'Id'),
         (u'char', u'Char (not implemented yet)'),
         (u'selection', u'Selection')],
        required=True
    )
    source_model_id = fields.Many2one(
        'etl.external_model',
        string='Source Model'
    )
    target_model_id = fields.Many2one(
        'etl.external_model',
        string='Target Model'
    )
    log = fields.Text(
        string='log'
    )
    value_mapping_field_detail_ids = fields.One2many(
        'etl.value_mapping_field_detail',
        'value_mapping_field_id',
        string='Details',
        help="This is te actual mapping between source and target."
    )
    value_mapping_field_value_ids = fields.One2many(
        'etl.value_mapping_field_value',
        'value_mapping_field_id',
        string='Mapping Values',
        help="These are all the values ​​that are going to be mapped, all of the source "
             "plus all of the target without repeating."
    )
    manager_id = fields.Many2one(
        'etl.manager',
        ondelete='cascade',
        required=True
    )

    def map_record(self):
        for rec in self:
            value_mapping_data = []
            for source_record in rec.source_model_id.external_model_record_ids:
                domain = [
                    ('external_model_id', '=', rec.target_model_id.id),
                    ('name', 'ilike', source_record.name)]
                target_record = self.env[
                    'etl.external_model_record'].search(domain, limit=1)
                value_mapping_data.append([
                    'value_mapping_' + str(source_record.id),
                    source_record.id,
                    target_record and target_record.id or False,
                    rec.id,
                ])

            value_mapping_fields = [
                'id',
                'source_external_model_record_id/.id',
                'target_external_model_record_id/.id',
                'value_mapping_field_id/.id']
            import_result = self.env['etl.value_mapping_field_detail'].load(
                value_mapping_fields, value_mapping_data)

            # write log and domain if active field exist
            rec.log = import_result
