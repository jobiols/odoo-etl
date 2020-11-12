import logging
from odoo import models
from odoo.tests.common import Form
_logger = logging.getLogger(__name__)

class AccountMove(models.Model):
    _inherit = 'account.move'

    def get_id(self, xml_id):
        """ Dado el xml_id id obtiene el id
        """
        model_obj = self.env['ir.model.data']
        xml_id = xml_id.split('.')
        _, _id = model_obj.get_object_reference(xml_id[0], xml_id[1])
        return _id

    def insert_invoice(self, param):
        """ Inserta las lineas de factura de una factura que viene en param
        """
        _logger.info('Inserting Invoice -------------------------------- ')

        def get_value(obj, xml_id):
            """ Dado el modelo y el xml_id devuelve el record
            """
            _id = self.get_id(xml_id)

            _logger.info('Convertir %s en %d' % (xml_id, _id))

            ret = obj.search([('id', '=', _id)])

            _logger.info('se encontro el record %s' % str(ret))

            return ret

        # modelos
        am_obj = self.env['account.move']
        partner_obj = self.env['res.partner']
        account_obj = self.env['account.account']
        product_obj = self.env['product.product']

        # suponiendo que todas las facturas estan migradas abro un Form con cada una
        # de las facturas
        move_form = Form(get_value(am_obj, param['move_id']))
        _logger.info('Creado el form con id %s ', param['move_id'])

        try:
            # recorremos las lineas de factura y procesamos cada una
            for line in param['lines']:

                # creamos una linea de factura sin salvarla en bd
                with move_form.invoice_line_ids.new() as line_form:
                    _logger.info('procesando la linea %s ', str(line))

                    # No se como usar el id de la linea, en este momento se creo una
                    # account_invoice_line pero con id = 0 todavia no esta en la bd.
                    unused = line['id']

                    line_form.product_id = get_value(product_obj, line['product_id/id'])
                    if line_form.product_id:
                        _logger.info('agregado producto %s', line_form.product_id.name)
                    else:
                        _logger.error('Product not found %s', line['product_id/id'])

                    line_form.discount = line['discount']
                    line_form.name = line['name']
                    line_form.quantity = line['quantity']
                    line_form.sequence = line['sequence']
                    line_form.price_unit = line['price_unit']

                    # no se para que esta el partner aca
                    line_form.partner_id = get_value(partner_obj, line['partner_id/id'])

                    # agregamos la cuenta contable
                    line_form.account_id = get_value(account_obj, line['account_id/id'])
                    if line_form.account_id:
                        _logger.info('account %s', line_form.account_id.name)
                    else:
                        _logger.info('NO account')

                    _logger.info('terminado de cargar los datos de la factura')

            # salvar la factura completa en la bd
            invoice = move_form.save()
            _logger.info('se salvo la factura con estos elementos %s', str(invoice.line_ids.ids))

            # devolver los ids de todas las lineas del asiento.
            return str(invoice.line_ids.ids)

        except Exception as ex:
            _logger.error('Error %s', (str(ex)))
            # ocurrio un error devolver el mensaje
            return str(ex)
