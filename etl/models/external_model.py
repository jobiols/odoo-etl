##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from ast import literal_eval
import logging
from odoo.osv import expression
from odoo import models, fields, api, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ExternalModel(models.Model):
    _name = 'etl.external_model'
    _description = 'external_model'
    _rec_name = 'd_name'
    _order = "sequence"

    sequence = fields.Integer(
        readonly=True
    )
    type = fields.Selection(
        [('source', 'Source'),
         ('target', 'Target')],
        readonly=True,
        required=True
    )
    name = fields.Char(
        readonly=True,
        required=True
    )
    model = fields.Char(
        readonly=True,
        required=True
    )
    d_name = fields.Char(
        compute="_compute_d_name",
        help="is the name shown as display_name on the views"
    )
    order = fields.Integer(
        readonly=True
    )
    records = fields.Integer(
        readonly=True
    )
    fields_to_read = fields.Char(
        default=['name']
    )
    field_ids = fields.One2many(
        'etl.field',
        'model_id',
        string='Fields',
        readonly=True
    )
    source_action_ids = fields.One2many(
        'etl.action',
        'source_model_id',
        string='source_action_ids'
    )
    target_action_ids = fields.One2many(
        'etl.action',
        'target_model_id',
        string='target_action_ids'
    )
    manager_id = fields.Many2one(
        'etl.manager',
        ondelete='cascade',
        string='Manager',
        readonly=True,
        required=True
    )
    external_model_record_ids = fields.One2many(
        'etl.external_model_record',
        'external_model_id',
        string='external_model_record_ids'
    )

    def _compute_d_name(self):
        for rec in self:
            rec.d_name = '%s (%s)' % (rec.name, rec.model) if rec.name != rec.model else rec.model

    def read_records(self):
        """ Function that reads external id and name field from an external
            model and save them in migrator database
        """

        for rec in self:
            source_connection, target_connection = \
                rec.manager_id.open_connections()
            if rec.type == 'source':
                connection = source_connection
            else:
                connection = target_connection

            fields_to_read = []
            if rec.fields_to_read:
                fields_to_read = literal_eval(rec.fields_to_read)

            record_fields = ['.id', 'id']

            record_fields.extend(fields_to_read)

            external_model_obj = connection.model(rec.model)
            external_model_record_ids = external_model_obj.search([])
            external_model_record_data = external_model_obj.export_data(
                external_model_record_ids, record_fields)['datas']

            new_external_model_record_data = []
            for record in external_model_record_data:
                # take out item o and init new_record with our own ext id
                new_record = ['model%i_record_%s' % (rec.id, record.pop(0))]
                # append readed external id 'id' to new record
                new_record.append(record.pop(0))
                # buid name wit readed fields
                name = ''
                # record = record.decode("utf-8")
                name = '; '.join([x for x in record if x])
                new_record.append(name)
                # append model id
                new_record.append(rec.id)
                new_external_model_record_data.append(new_record)
            external_model_record_fields = [
                'id',
                'ext_id',
                'name',
                'external_model_id/.id']
            # load records
            self.env['etl.external_model_record'].load(
                external_model_record_fields, new_external_model_record_data)

    def read_fields_button(self):
        return self.read_fields(False)

    def read_fields(self, connection=False):
        """ Get fields for external models
        """
        field_fields = [
            'id',
            'model_id/.id',
            'field_description',
            'name',
            'relation',
            'required',
            'ttype',
            'function']
        model_field_data = []
        for model in self:
            _logger.info('Reading fields from %s model: %s', model.type, model.display_name)
            if not connection:
                source_connection, target_connection = model.manager_id.open_connections()
                if model.type == 'source':
                    connection = source_connection
                elif model.type == 'target':
                    connection = target_connection
                else:
                    raise UserError(_('Error getting connection'))
            try:
                external_model_obj = connection.model(model.model)
            except Exception as ex:
                _logger.info('Model database, model: %s not found !!!',
                             model.model)
                continue
            try:
                external_model_fields = external_model_obj.fields_get()
            except Exception as ex:
                _logger.info('fields_get error: %s', str(ex))
                continue
            else:
                for field in external_model_fields:
                    field_dic = external_model_fields[field]
                    name = field
                    string = field_dic.get('string' or False)
                    function = field_dic.get('function' or False)
                    ttype = field_dic.get('type' or False)
                    relation = field_dic.get('relation' or False)
                    required = field_dic.get('required' or False)

                    field_data = [
                        'field_model_%s_%s' % (str(model.id), name),
                        model.id,
                        string,
                        name,
                        relation,
                        required,
                        ttype,
                        function
                    ]
                    model_field_data.append(field_data)

        _logger.info('Writing fields data...')
        self.env['etl.field'].load(field_fields, model_field_data)

    def get_record_count(self, connection, domain='[]'):
        """ Get the number of records of this external model
            Si no encuentro el record es porque no esta el modelo, no es un
            error grave, puedo agregar el modelo y volver a correr.
        """

        for rec in self:
            try:
                _logger.info('%i records on model %s', rec.records, rec.display_name)
                model_obj = connection.model(rec.model)
                rec.records = model_obj.search_count(literal_eval(domain))
            except Exception as ex:
                rec.records = -1
                _logger.warning('Error %s retrieving number of records in model %s',
                                str(ex), rec.model)
