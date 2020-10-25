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

        def get_value(obj, xml_id):
            _id = self.get_id(xml_id)
            return obj.search([('id', '=', _id)])

        # modelos
        am_obj = self.env['account.move']
        partner_obj = self.env['res.partner']
        account_obj = self.env['account.account']
        product_obj = self.env['product.product']
        acc_obj = self.env['account.account']

        # suponiendo que todas las facturas estan migradas abro un Form con cada una
        # de las facturas
        move_form = Form(get_value(am_obj, param['move_id']))

        # Variable para devolver errores, las excepciones no burbujean desde aqui.
        err = ''
        try:
            # recorremos las lineas de factura y procesamos cada una
            for line in param['lines']:

                # creamos una linea de factura sin salvarla en bd
                with move_form.invoice_line_ids.new() as line_form:

                    # No se como usar el id de la linea, en este momento se creo una
                    # account_invoice_line pero con id = 0 todavia no esta en la bd.
                    unused = line['id']

                    # Todos los productos tienen que estar migrados
                    # por ahora le pongo un producto cualquiera.
#                    line_form.product_id = get_value(product_obj, line['product_id/id']) # para las pruebas le mando cualquiera
                    line_form.product_id = product_obj.search([], limit=1)

                    line_form.discount = line['discount']
                    line_form.name = line['name']
                    line_form.quantity = line['quantity']
                    line_form.sequence = line['sequence']
                    line_form.price_unit = line['price_unit']

                    # no se para que esta el partner aca
                    line_form.partner_id = get_value(partner_obj, line['partner_id/id'])

                    # todas las cuentas contables deben estar migradas, por ahora le
                    # pongo una cuenta cualquiera
   #                line_form.account_id = get_value(account_obj, line['account_id/id'])
                    line_form.account_id = account_obj.search([], limit=1)

        except Exception as ex:
            return str(ex)

        # salvar la factura completa en la bd
        invoice = move_form.save()

        # devolver los ids de las lineas de factura que salve.
        return str(invoice.invoice_line_ids.ids)
