#
##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import models, fields


class Field(models.Model):
    _name = 'etl.field'
    _description = 'Field'

    name = fields.Char(
        required=True
    )
    field_description = fields.Char(
        required=True
    )
    relation = fields.Char(

    )
    relation_field = fields.Char(
    )
    ttype = fields.Char(
        string='TType',
        required=True
    )
    required = fields.Char(

    )
    function = fields.Char(

    )
    model_id = fields.Many2one(
        'etl.external_model',
        ondelete='cascade',
        string='Model'
    )
    type = fields.Selection(
        related='model_id.type',
        readonly=True,
    )

    # def _name_search(self, cr, uid, name='', args=None, operator='ilike',
    #     context=None, limit=100, name_get_uid=None):
    #     if args is None:
    #         args = []
    #     domain = args + ['|',
    #                      ('field_description', operator, name),
    #                      ('name', operator, name)]
    #     return self.name_get(cr, name_get_uid or uid,
    #                          super(Field, self).search(cr, uid, domain,
    #                                                    limit=limit,
    #                                                    context=context),
    #                          context=context)
