#
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
import time
import logging
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)


class FieldMapping(models.Model):
    _name = 'etl.field_mapping'
    _description = 'field_mapping'

    blocked = fields.Boolean(
        default=False
    )
    type = fields.Selection(
        [('field', 'Field'),
         ('expression', 'Expression'),
         ('migrated_id', 'Migrated ID'),
         ('value_mapping', 'Value Mapping'),
         ('date_adapt', 'Date Adapt'),
         ('reference', 'Reference')],
        string='Mapping Type',
        default='field',
        help="Field: move data between two fields\n"
             "Expression: \n"
             "Migrated ID: \n"
             "Value Mapping: \n"
             "Date Adapt: \n"
             "Reference: \n"
    )
    state = fields.Selection(
        [('on_repeating', 'On Repeating'),
         ('to_analyze', 'To Analyze'),
         ('enabled', 'Enabled'),
         ('disabled', 'Disabled'),
         ('other_class', 'Other Class')],
        required=True
    )
    source_field_id = fields.Many2one(
        'etl.field',
    )
    source_field = fields.Char(
        string='Source Field.',
        help="Name of the Tource Field."
    )
    target_field_id = fields.Many2one(
        'etl.field',
    )
    target_field = fields.Char(
        string='Target Field.',
        help="Name of the Target Field"
    )
    expression = fields.Text(
        default="context['result']= False"
    )
    value_mapping_field_id = fields.Many2one(
        'etl.value_mapping_field',
        string='Value Mapping Field'
    )
    model_field_id = fields.Many2one(
        'etl.field',
        string='Model Field'
    )
    model_field = fields.Char(
        string='Model Field Exp.'
    )
    note = fields.Html(
        string='Notes'
    )
    action_id = fields.Many2one(
        'etl.action',
        ondelete='cascade',
        string='Action',
        required=True
    )
    target_model_id = fields.Many2one(
        related='action_id.target_model_id',
        relation='etl.external_model',
        string='Target Model',
    )
    source_model_id = fields.Many2one(
        related='action_id.source_model_id',
        relation='etl.external_model',
        string='Source Model',
    )
    source_field_ttype = fields.Char(
        related='source_field_id.ttype',
        readonly=True,
        string='Source TType'
    )
    target_field_ttype = fields.Char(
        related='target_field_id.ttype',
        readonly=True,
        string='Target Type'
    )
    manager_id = fields.Many2one(
        related='action_id.manager_id',
        relation='etl.manager',
        readonly=True,
        string='Manager'
    )

    @api.onchange('source_field_id')
    def onchange_source_field(self):
        self.source_field = False
        if self.source_field_id:
            self.source_field = self.source_field_id.name
            if self.source_field_id.ttype in ['many2one', 'many2many', 'one2many']:
                self.source_field += '/id'

    @api.onchange('target_field_id')
    def onchange_target_field(self):
        self.target_field = False
        if self.target_field_id:
            self.target_field = self.target_field_id.name
            if self.target_field_id.ttype in ['many2one', 'many2many', 'one2many']:
                self.target_field += '/id'

    def action_block(self):
        return self.write({'blocked': True})

    def get_migrated_id(self, rec_id, source_connection=False, target_connection=False):
        """ Get migrated id for field ids and one rec_id (from source database)
            For example, for field mapping ids
        """
        result = []

        for field_mapping in self:
            if not source_connection or not target_connection:
                source_connection, target_connection = field_mapping.action_id.manager_id.open_connections()
            source_model_obj = source_connection.model(field_mapping.action_id.source_model_id.model)
            target_ir_model_data_obj = target_connection.model('ir.model.data')

            source_fields = ['id', field_mapping.source_field_id.name, field_mapping.model_field]

            _logger.info('Source_fields: %s', source_fields)
            source_model_data = source_model_obj.export_data([rec_id], source_fields)['datas']

            _logger.info('Source_model_data: %s', source_model_data)
            target_id = False
            if source_model_data:
                source_id = source_model_data[0][1]
                try:
                    source_resource_obj = source_connection.model(
                        source_model_data[0][2])
                except Exception as ex:
                    target_id = False
                    _logger.info('Exception 158: %s', str(ex))
                else:
                    source_reference = source_resource_obj.export_data(
                        [int(source_id)], ['id'])['datas']
                    if source_reference[0]:
                        source_reference_splited = source_reference[0][0].split('.', 1)
                        if len(source_reference_splited) == 1:
                            module = False
                            external_ref = source_reference_splited[0]
                        else:
                            module = source_reference_splited[0]
                            external_ref = source_reference_splited[1]
                        try:
                            # cambiamos a esta manera fea porque el metodo de
                            # abajo no andaba
                            target_ids = target_ir_model_data_obj.search([
                                ('module', '=', module),
                                ('name', '=', external_ref)])
                            target_ids = target_ir_model_data_obj.read(
                                target_ids, ['res_id'])
                            if target_ids:
                                target_id = target_ids[0].get('res_id', False)
                                # target_id = target_ir_model_data_obj.g
                                # et_object_reference(
                                # module, external_ref)[1]
                        except Exception as ex:
                            target_id = False
                            _logger.info('Exception 186: %s', str(ex))

            result.append(target_id)
        return result

    def get_reference(self, rec_id, source_connection=False, target_connection=False):
        """ Get reference for field ids  and one rec_id (from source database)
            For example, for field mapping ids
        """

        result = []
        for field_mapping in self:
            if not source_connection or not target_connection:
                (source_connection, target_connection) = \
                    field_mapping.action_id.manager_id.open_connections()
            source_model_obj = source_connection.model(
                field_mapping.action_id.source_model_id.model)
            target_ir_model_data_obj = target_connection.model('ir.model.data')
            source_fields = [field_mapping.source_field_id.name]
            source_model_data = source_model_obj.read(
                [rec_id], source_fields)[0]
            target_id = False
            if source_model_data:
                source_reference = source_model_data[
                    field_mapping.source_field_id.name]
                if source_reference:
                    model, res_id = source_reference.split(',', 1)
                    try:
                        source_resource_obj = source_connection.model(model)
                    except Exception as ex:
                        _logger.info('Exception 216: %s', str(ex))
                        target_id = False
                    else:
                        source_ext_id = source_resource_obj.export_data(
                            [res_id], ['id'])['datas']
                        if source_ext_id[0]:
                            source_ext_id_splited = source_ext_id[0][0].split(
                                '.', 1)
                            if len(source_ext_id_splited) == 1:
                                module = False
                                external_ref = source_ext_id_splited[0]
                            else:
                                module = source_ext_id_splited[0]
                                external_ref = source_ext_id_splited[1]
                            try:
                                target_id = target_ir_model_data_obj.get_object_reference(module, external_ref)[1]  # noqa
                            except Exception as ex:
                                # Agregamos este nuevo try porque algunas
                                # veces module no es false si no que es como
                                # una cadena vacia
                                _logger.info('Exception 236: %s', str(ex))
                                try:
                                    target_id = target_ir_model_data_obj.get_object_reference('', external_ref)[1]  # noqa
                                except Exception as ex:
                                    target_id = False
                                    _logger.info('Exception 241: %s', str(ex))

            target_reference = False
            if target_id:
                target_reference = model + ',' + str(target_id)
            result.append(target_reference)
        return result

    def run_expressions(self, rec_id, source_connection=False, target_connection=False):
        result = []

        for field_mapping in self:
            expression_result = False
            if not source_connection or not target_connection:
                source_connection, target_connection = field_mapping.action_id.manager_id.open_connections()

            source_model_obj = source_connection.model(field_mapping.action_id.source_model_id.model)
            target_model_obj = target_connection.model(field_mapping.action_id.target_model_id.model)

            obj_pool = source_model_obj
            cxt = {
                'self': obj_pool,  # to be replaced by target_obj
                'source_obj': source_model_obj,
                'source_connection': source_connection,
                'target_obj': target_model_obj,
                'target_connection': target_connection,
                'rec_id': rec_id,
                'env': self.env,
                'time': time,
                'cr': self._cr,
                # copy context to prevent side-effects of eval
                'context': dict(self._context),
                'uid': self.env.user.id,
                'user': self.env.user,
            }
            if not field_mapping.expression:
                raise UserError(_("Warning. Type expression choosen but not expression "
                                  "set"))
            # nocopy allows to return 'action'
            safe_eval(field_mapping.expression.strip(), cxt, mode="exec")
            if 'result' in cxt['context']:
                expression_result = cxt['context'].get('result')
            result.append(expression_result)
        return result
