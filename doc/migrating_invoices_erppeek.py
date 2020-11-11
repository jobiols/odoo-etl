from erppeek import Client

target = {
    'host':'https://patriciopa-odoo13-demo-main-1595300.dev.odoo.com',
    'db': 'patriciopa-odoo13-demo-main-1595300',
    'user': 'admin',
    'password': 'elias'
}

source = {
    'host':'http://10.254.128.237:8069',
    'db': 'consulting_backup_3',
    'user': 'alexis@quilsoft.com',
    'password': 'Quilsoft1234'
}

def _get_target():
    conn = Client(target['host'], db=target['db'], user=target['user'], password=target['password'])
    model = conn.model('res.country.state')
    ids = model.search([])
    fields = ['id/id', 'country_id/id', 'name']
    datas = model.export_data(ids, fields)['datas']
    for data in datas:
        print(data)

def _get_source():
    "Traer todos los identificadores externos de res.partner.state"

    conn = Client(source['host'], db=source['db'], user=source['user'], password=source['password'])

    model = conn.model('res.partner')
    rec_id = 2556
    is_customer = model.export_data([rec_id], ['customer'])['datas'][0][0]



    ids = model.search([('country_id.name', '=', 'Chile')])

    fields = ['id/id', 'country_id/id', 'name']
    datas = model.export_data(ids, fields)['datas']
    for data in datas:
        print(data)

_get_source()

