from odoo import models
from odoo.tests.common import Form

class AccountMove(models.Model):
    _inherit = 'account.move'

    def insert_invoice(self, param):

        move_id = param['move_id']
        lines = param['lines']

        move_form = Form(self.env['account.move'].with_context(default_type='out_invoice'))
        import wdb;wdb.set_trace()

        move_form.partner_id = self.env['res.partner'].search([('id', '=', 1263)])

        with move_form.invoice_line_ids.new() as line_form:
            line_form.product_id = self.env['product.product'].search([], limit=1)
        with move_form.invoice_line_ids.new() as line_form:
            line_form.product_id = self.env['product.product'].search([], limit=1)
        move = move_form.save()

        return True
