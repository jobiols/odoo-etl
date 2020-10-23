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

args = {'move_id': 198, 'lines': [3, 4, 5]}

conn.execute('account.move', 'insert_move_lines', 1, args)
