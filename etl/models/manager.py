#
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields, _
from odoo.exceptions import UserError
from erppeek import Client
from ast import literal_eval
import logging

_logger = logging.getLogger(__name__)


class Manager(models.Model):
    _name = 'etl.manager'
    _description = 'etl manager'

    name = fields.Char(
        required=True,
        help='Contains the name of your manager without any specific '
               'restriction.'
    )
    target_id_type = fields.Selection(
            [(u'source_id', 'Source ID'),
             (u'builded_id', 'Builded ID')],
        string='Target ID Type',
        required=True,
        default='source_id',
        help='Selection on how the Target Records ID''s will be build:\n'
             'Source ID will keep the ID (external_id) from the source.\n'
             'Builded ID - every external ID will be build as concatenation '
             'of Manager Name + _ + Source Model.\n'
             ' Source ID is recommended when performing a migration process.'
    )
    source_hostname = fields.Char(
        required=True,
        default='http://localhost',
        help='The source database host URL that is used to access the Odoo '
             'database from remote OS. i.e.: http://192.168.1.101.'
    )
    source_port = fields.Integer(
        required=True,
        default=80,
        help='The source database port that is used to access the Odoo '
             'database. i.e.: 8069.'
    )
    source_database = fields.Char(
        string='Source Database',
        required=True,
        help='The source database name'
    )
    source_login = fields.Char(
        required=True,
        help='The username used to login to the source database from the '
             'login page. Make sure this user have full access to all the '
             'models.'
    )
    source_password = fields.Char(
        required=True,
        help='the password, what else?.'
    )
    source_lang = fields.Char(
        'Source Language',
        required=True,
        default='en_US',
        # TODO improove this and load all translations for tranlatable fields
        help='The source database default language. It’s recommended to keep '
             'the language as default (en_US)'
    )
    target_hostname = fields.Char(
        required=True,
        default='http://localhost',
        help='the target database host URL that is used to access the Odoo '
             'database from remote OS. i.e.: http://192.168.1.101.'
    )
    target_port = fields.Integer(
        required=True,
        default=80,
        help='The target database port that is used to access the Odoo '
             'database. i.e.: 8069.'
    )
    target_database = fields.Char(
        required=True,
        help='the target database name.'
    )
    target_login = fields.Char(
        required=True,
        help='the username used to login to the target database from the '
             'login page. Make sure this user have full access to all the '
             'models.'
    )
    target_password = fields.Char(
        required=True,
        help='the password, what else?.'
    )
    log = fields.Text(

    )
    model_disable_default = fields.Text(
        string='Models Disabled by Default',
        # TODO move this default to another model
        default="['ir.model','ir.model.fields','ir.model.access',"
                "'ir.model.data','ir.sequence.type','ir.sequence',"
                "'ir.ui.menu','ir.ui.view.custom','ir.ui.view',"
                "'ir.ui.view_sc','ir.default','ir.actions.actions',"
                "'ir.actions.act_window','ir.actions.act_window.view',"
                "'ir.actions.wizard','ir.actions.url','ir.server.object.lines'"
                ",'ir.actions.server','ir.actions.act_window_close',"
                "'ir.actions.todo.category','ir.actions.todo',"
                "'ir.actions.client','ir.values','ir.translation',"
                "'ir.exports','ir.exports.line','workflow','workflow.activity'"
                ",'workflow.transition','workflow.instance',"
                "'workflow.workitem','workflow.triggers','ir.rule',"
                "'ir.module.category','ir.module.module',"
                "'ir.module.module.dependency','res.widget','res.widget.user',"
                "'publisher_warranty.contract','ir.module.record',"
                "'board.board','board.board.line','decimal.precision',"
                "'process.process','process.node','process.condition',"
                "'process.transition','process.transition.action',"
                "'email_template.preview','account.tax.template',"
                "'account.account.template','account.tax.code.template',"
                "'account.chart.template','account.fiscal.position.template',"
                "'account.fiscal.position.tax.template',"
                "'account.fiscal.position.account.template','temp.range',"
                "'mrp.property.group','mrp.property',"
                "'account.invoice.ar.installer','pos.config.journal',"
                "'oo.config','mass.object','mass.editing.wizard',"
                "'support.support_contract','support.email',"
                "'account_analytic_analysis.summary.user',"
                "'account_analytic_analysis.summary.month','res.groups',"
                "'mail.alias']"
    )
    field_disable_default = fields.Text(
        string='Fields Disable by Default',
        # TODO move this default to another model
        default="['lang','printed_vat','context_lang','context_department_id',"
                "'groups_id','alias_defaults','alias_id','alias_model_id',"
                "'create_date','calendar_last_notif_ack',]",
    )
    model_exception_words = fields.Char(
        # TODO parecen ser los modelos que no queremos cargar jeo.
        # TODO move this default to another model
        default="['report','ir.logging','ir.qweb']",
    )
    model_wanted_words = fields.Char(
        # TODO parecen ser los modelos que queremos cargar jeo.
        # TODO move this default to another model
        # TODO Tener en cuenta que pueden llamarse distinto en distintas vers
        default="['res.partner','res.partner.category','res.partner.industry','res.company','res.partner.title','res.users']"
    )

    model_analyze_default = fields.Text(
        string='Models Analyze by Default',
        # TODO move this default to another model
        default="['ir.attachment','ir.cron','ir.filters',"
                "'ir.config_parameter','ir.mail_server','res.country',"
                "'res.country.state','res.lang','res.currency',"
                "'res.currency.rate.type','res.currency.rate',"
                "'multi_company.default','res.company','res.users',"
                "'res.request','res.request.link','res.request.history',"
                "'res.log','ir.property','mail.message','mail.thread',"
                "'product.uom.categ','product.uom','product.ul',"
                "'product.price.type','product.pricelist.type',"
                "'base.action.rule','email.template','fetchmail.server',"
                "'edi.document','account.tax','account.account',"
                "'account.journal.view','account.journal.column',"
                "'account.fiscalyear','account.period',"
                "'account.journal.period','account.analytic.journal',"
                "'account.fiscal.position','account.fiscal.position.tax',"
                "'account.fiscal.position.account',"
                "'account.sequence.fiscalyear','procurement.order',"
                "'sale.shop','document.storage','document.directory',"
                "'document.directory.dctx','document.directory.content.type',"
                "'document.directory.content','account.voucher',]",
    )
    note = fields.Html(
        string='Notes'
    )
    field_analyze_default = fields.Text(
        string='Fields Analize by Default',
        # TODO move this default to another model
        default="['reconcile_partial_id','reconcile_id']",
    )
    repeating_models = fields.Text(
        # TODO move this default to another model
        default="['res.partner','res.company','res.users',"
                "'account.fiscalyear','product.template','product.product',"
                "'purchase.order','sale.order','hr.employee','project.task',"
                "'procurement.order']",
    )
    field_disable_words = fields.Text(
        string='Fields Disable by Default Words',
        # TODO move this default to another model
        default="['in_group','sel_groups_','rml_header','rml_foot',]",
    )
    modules_to_install = fields.Text(
        default=[]
    )
    workflow_models = fields.Char(
        string='Models to delete Workflows',
        required=True,
        default='[]'
    )
    action_ids = fields.One2many(
        'etl.action',
        'manager_id',
        string='Actions',
        domain=[('state', 'in', ['to_analyze', 'enabled'])],
        copy=False,
    )
    external_model_ids = fields.One2many(
        'etl.external_model',
        'manager_id',
        string='External Models',
        readonly=True,
        copy=False,
    )
    value_mapping_field_ids = fields.One2many(
        'etl.value_mapping_field',
        'manager_id',
        string='Value Mapping Fields',
        copy=False,
    )
    target_lang = fields.Char(
        'Target Language',
        required=True,
        default='en_US',
        # TODO improove this and load all translations for tranlatable fields
        help='the target database default language. It’s recommended to keep '
             'the language as default (en_US).'
    )
    # odoo_target_version = fields.Integer(
    #     default=lambda self: self.get_current_version(),
    #     required=True,
    #     help='the target odoo major version, default is the odoo version '
    #     'where this module is installed'
    # )
    # odoo_source_version = fields.Integer(
    #     required=True,
    #     default=8,
    #     help='the source odoo major version, default 8'
    # )

    # def get_current_version(self):
    #     base = self.env['ir.module.module']
    #     ver = base.search([('name', '=', 'base')]).latest_version
    #     return int(ver[:ver.find('.')])

    def open_connections(self):
        self.ensure_one()
        try:
            _logger.info('Getting source connection')
            source_connection = Client(
                '%s:%i' % (self.source_hostname, self.source_port),
                db=self.source_database,
                user=self.source_login,
                password=self.source_password)
        except Exception as ex:
            raise UserError(
                _("Unable to Connect to Source Database. 'Error: %s'") % ex)
        try:
            _logger.info('Getting target connection')
            target_connection = Client(
                '%s:%i' % (self.target_hostname, self.target_port),
                db=self.target_database,
                user=self.target_login,
                password=self.target_password)
        except Exception as ex:
            raise UserError(
                _("Unable to Connect to Target Database. 'Error: %s'") % ex)
        return [source_connection, target_connection]

    def read_active_source_models(self):
        for rec in self:
            source_connection, target_connection = self.open_connections()
            domain = [('manager_id', '=', rec.id), ('state', '=', 'enabled')]
            actions = self.env['etl.action'].search(domain, order='sequence')
            actions.read_source_model(source_connection, target_connection)

    def delete_workflows(self):
        for rec in self:
            (source_connection, target_connection) = self.open_connections()
            target_wf_instance_obj = target_connection.model('workflow.instance')  # noqa
            res_types = literal_eval(rec.workflow_models)
            target_wf_instance_ids = target_wf_instance_obj.search(
                [('res_type', 'in', res_types)])
            target_wf_instance_obj.unlink(target_wf_instance_ids)

    def install_modules(self):
        for rec in self:
            source_connection, target_connection = self.open_connections()
            target_module_obj = target_connection.model("ir.module.module")
            try:
                modules = literal_eval(rec.modules_to_install)
            except ValueError:
                raise UserError('Enter the technical names of the modules '
                                 'to install in quotes and comma separated '
                                 'with the syntax of a python list.\n\n'
                                 'i.e. ["crm","stock","hr"]')
            domain = [('name', 'in', modules)]
            target_module_ids = target_module_obj.search(domain)
            target_module_obj.button_immediate_install(target_module_ids)

    def run_actions(self):
        """ Run all actions (none repeating)
        """
        for rec in self:
            domain = [('manager_id', '=', rec.id), ('state', '=', 'enabled')]
            actions = self.env['etl.action'].search(domain, order='sequence')
            actions.run_action()

    def run_repeated_actions(self):
        """ Run all repeating actions
        """
        for rec in self:
            actions = self.env['etl.action'].search([
                ('manager_id', '=', rec.id),
                ('repeating_action', '=', True),
                ('state', '=', 'enabled')],
                                                    order='sequence')
            actions.run_repeated_action()

    def match_models_and_order_actions(self):
        """ Match models and order the actions
        """
        for rec in self:
            rec.match_models()
            rec.order_actions()

    def match_models(self):
        """ Match models """
        for rec in self:
            _logger.info('Matching models for manager %s', rec.name)
            # read all source models
            source_domain = [('manager_id', '=', rec.id), ('type', '=', 'source')]
            source_models = self.env['etl.external_model'].search(source_domain)

            # get disable and to analyze models
            data = []
            model_disable_default = []
            model_analyze_default = []
            if rec.model_disable_default:
                model_disable_default = literal_eval(rec.model_disable_default)
            if rec.model_analyze_default:
                model_analyze_default = literal_eval(rec.model_analyze_default)

            # get blocked external ids models
            blocked_models = self.env['etl.action'].search(
                [('blocked', '=', True), ('manager_id', '=', self.id)])
            blocked_model_ext_ids = blocked_models.export_data(['id'])['datas']

            # for each source model look for a target model and give state
            for model in source_models:
                target_domain = [
                    ('manager_id', '=', rec.id),
                    ('type', '=', 'target'), ('model', '=', model.model)]
                target_model = self.env['etl.external_model'].search(
                    target_domain, limit=1)

                # give right state to model mapping
                state = 'enabled'
                if model.model in model_disable_default:
                    state = 'disabled'
                elif model.model in model_analyze_default or not target_model:
                    state = 'to_analyze'
                if model.records == 0:
                    state = 'no_records'

                # get vals for action mapping and create and id
                vals = [
                    'model_mapping_' + str(rec.id) + '_' + str(model.id),
                    state,
                    model.name + ' (' + model.model + ')',
                    model.order,
                    model.id,
                    target_model and target_model.id or False,
                    rec.id
                ]

                # look if this id should be blocked
                if [vals[0]] in blocked_model_ext_ids:
                    continue

                # append if not to data
                data.append(vals)

            # write actions with data an fields, give result to log
            action_fields = [
                'id', 'state', 'name', 'sequence', 'source_model_id/.id',
                'target_model_id/.id', 'manager_id/.id'
            ]
            _logger.info('Loading actions match for manager %s', rec.name)
            import_result = self.env['etl.action'].load(action_fields, data)

            # write log on manager
            rec.log = import_result

            # call for match fields
            _logger.info('Matching fields for models %s of manager %s',
                         import_result['ids'], rec.name)
            self.env['etl.action'].browse(import_result['ids']).match_fields()

    def order_actions(self):
        """ Order actions for ids managers. """
        for rec in self:
            # Get enabled actions
            actions = self.env['etl.action'].search([
                ('manager_id', '=', rec.id),
                ('state', 'in', ['to_analyze', 'enabled'])])

            # If repeating_models defined on the manager, take them as exceptions
            exceptions = []
            if rec.repeating_models:
                repeating_models = rec.repeating_models
                exceptions = literal_eval(repeating_models)

            # Get unordered and ordered ids from action model
            unordered_ids, ordered_ids = actions.order_actions(exceptions)

            # get unordered and ordered actions names to write in log. Write log
            ordered_actions = []
            unordered_actions = []

            for ordered_action in self.env['etl.action'].browse(ordered_ids):
                ordered_actions.append(ordered_action.source_model_id.model)
            for unordered_action in self.env['etl.action'].browse(unordered_ids):
                unordered_actions.append(unordered_action.source_model_id.model)
            rec.log = 'Ordered actions: %s\n\nUnordered actions: %s' % (
                str(ordered_actions), str(unordered_actions))

            # check actions depends if no unordered_ids
            if not unordered_ids:
                actions.check_m2o_depends()

    def read_and_get(self):
        """ Read source and target models and get records number
        """
        self.ensure_one()
        self.read_models()
        self.get_records()

    def get_records(self):
        """ Get number of records for source and target models
        """
        for rec in self:
            source_connection, target_connection = self.open_connections()

            domain = [('type', '=', 'source'), ('manager_id', '=', rec.id)]
            source_models = self.env['etl.external_model'].search(domain)

            domain = [('type', '=', 'target'), ('manager_id', '=', rec.id)]
            target_models = self.env['etl.external_model'].search(domain)

            source_models.get_records(source_connection)
            target_models.get_records(target_connection)

    def read_models(self):
        """ Get models and fields of source and target database
        """
        for rec in self:
            (source_connection, target_connection) = self.open_connections()
            rec.read_model(source_connection, 'source')
            rec.read_model(target_connection, 'target')

            source_external_models = rec.env['etl.external_model'].search([
                ('manager_id', '=', rec.id), ('type', '=', 'source')])

            target_external_models = rec.env['etl.external_model'].search([
                ('manager_id', '=', rec.id), ('type', '=', 'target')])

            source_external_models.read_fields(source_connection)
            target_external_models.read_fields(target_connection)

    def read_model(self, connection, relation_type):
        """ Get models for one manger and one type (source or target)
        """
        res = {}
        for manager in self:
            external_model_obj = connection.model("ir.model")

            # obtener la main version del odoo que estamos accediendo
            # base_obj = connection.model('ir.module.module')
            # ids = base_obj.search([('name', '=', 'base')])
            # data = base_obj.export_data(ids, ['latest_version'])
            # data = data['datas'][0][0]
            # ver = int(data[:data.find('.')])
            ver = int(float(connection.major_version))

            # TODO en 12 es models.TransientModel ver que hacemos con esto
            # osv_memory = False for not catching transients models
            if ver == 8:
                domain = [('osv_memory', '=', False)]
            else:
                domain = []
            
            # catch de models exceptions words and append to search domain
            # words_exception = manager.model_exception_words
            # if words_exception:
            #     words_exception = literal_eval(words_exception)
            #     for exception in words_exception:
            #         domain.append(('model', 'not like', exception))

            # catch the models to load and append to search domain
            words_wanted = manager.model_wanted_words
            if words_wanted:
                words_wanted = literal_eval(words_wanted)
                domain.append(('model', 'in', words_wanted))

            # get external model ids
            external_model_ids = external_model_obj.search(domain)

            # read id, model and name of external models
            external_model_fields = ['.id', 'model', 'name']
            export_data = external_model_obj.export_data(
                external_model_ids, external_model_fields)

            # We fix .id to id because we are going to use it
            external_model_fields[0] = 'id'

            # We add the type, manager and sequence to external fields and data
            external_model_fields.extend(
                ['type', 'manager_id/.id', 'sequence'])
            external_model_data = []
            for record in export_data['datas']:
                # we extend each record with type, manager and a sequence
                record.extend([relation_type, manager.id, int(record[0]) * 10])
                # replace the .id with our own external identifier
                record[0] = 'man_%s_%s_%s' % (
                    str(manager.id),
                    relation_type,
                    str(record[1]).replace('.', '_')
                )
                external_model_data.append(record)

            # Load external_model_data to external models model
            rec_ids = self.env['etl.external_model'].load(
                external_model_fields, external_model_data)
            res[manager.id] = rec_ids
        return res
