from odoo import models
from odoo.tests.common import Form

class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_id(self, external_id):
        _id = external_id.split('.')
        model_data = self.env['ir.model.data']
        _, res_id = model_data.get_object_reference(_id[0], _id[1])
        return res_id

    def unlink_invoice(self):
        _am = self.env['account.move'].search([])
        _am.unlink()

    def insert_invoice(self, param):

        am_obj = self.env['account.move']
        partner_obj = self.env['res.partner']
        account_obj = self.env['account.account']
        product_obj = self.env['product.product']
        acc_obj = self.env['account.account']

        _id = self.get_id(param['move_id'])
        move_form = Form(am_obj.search([('id', '=', _id)]))

        def get_value(obj, xml_id):
            _id = self.get_id(xml_id)
            return obj.search([('id', '=', _id)])

        err = ''
        try:
            for line in param['lines']:
                with move_form.invoice_line_ids.new() as line_form:
                    # el id no se pone
                    line_form.discount = line['discount']

                    #line_form.move_id = get_value(am_obj, line['move_id/id'])

                    line_form.name = line['name']
                    line_form.partner_id = get_value(partner_obj, line['partner_id/id'])
                    line_form.price_unit = line['price_unit']

   #                line_form.product_id = get_value(product_obj, line['product_id/id'])
                    line_form.product_id = product_obj.search([],limit=1)

   #                line_form.account_id = get_value(account_obj, line['account_id/id'])
                    line_form.account_id = account_obj.search([],limit=1)

                    line_form.quantity = line['quantity']
                    line_form.sequence = line['sequence']


        except Exception as ex:
            err = str(ex)

        invoice = move_form.save()
        import wdb;wdb.set_trace()

        return err
