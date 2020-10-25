from erppeek import Client

target = {
    'host':'https://patriciopa-odoo13-demo-main-1595300.dev.odoo.com',
    'db': 'patriciopa-odoo13-demo-main-1595300',
    'user': 'admin',
    'password': 'elias'
}

target = {
    'host':'http://localhost:8069',
    'db': 'migracion_consulting',
    'user': 'admin',
    'password': 'admin'
}

conn = Client(target['host'], db=target['db'], user=target['user'],
              password=target['password'])

args = {'move_id': '__export__.account_move_2_6b3c4b6f',
        'partner_id': '__export__.res_partner_1184',
        'type': 'out_invoice',
        'lines': [
            {'product_id': '__export__.product_template_1519'}
        ]
        }

conn.execute('account.move', 'insert_invoice', 1, args)
