from erppeek import Client

target = {
    'host':'https://patriciopa-odoo13-demo-main-1595300.dev.odoo.com',
    'db': 'patriciopa-odoo13-demo-main-1595300',
    'user': 'admin',
    'password': 'elias'
}

source = {
    'host':'http://10.254.128.237:8069',
    'db': 'consulting_backup_5',
    'user': 'alexis@quilsoft.com',
    'password': 'Quilsoft1234'
}

def _get_target():
    conn = Client(target['host'], db=target['db'], user=target['user'], password=target['password'])
    model = conn.model('account.move')
    ids = model.search([])
    datas = model.export_data(rec_ids, ['account_id/id'])['datas']

    datas = model.execute('action_post')

def get_source_data():
    conn = Client(source['host'], db=source['db'], user=source['user'], password=source['password'])

    model = conn.model('account.invoice')
    rec_ids = model.search([('id', '<', 140)])
    print(len(rec_ids))

    return model.export_data(rec_ids, ['id/id','state'])['datas']


def post_invoices():
    conn = Client(target['host'], db=target['db'], user=target['user'], password=target['password'])

    # Draft, Pro-forma, Open, Paid, Cancelled

    datas = get_source_data()
    for data in datas:
        ret = conn.execute('account.move', 'post_invoices', 1, {'param': data})
        print(data)
        print(ret)

post_invoices()
