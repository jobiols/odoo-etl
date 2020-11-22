from erppeek import Client

target = {
    'host':'https://githubconsultingcs-cservices2-staging02-1706737.dev.odoo.com/',
    'db': 'githubconsultingcs-cservices2-staging02-1706737',
    'user': 'admin',
    'password': 'adminsh'
}

source = {
    'host':'http://10.254.128.237:8069',
    'db': 'consulting_backup_5',
    'user': 'alexis@quilsoft.com',
    'password': 'Quilsoft1234'
}

def get_source_data():
    conn = Client(source['host'], db=source['db'], user=source['user'], password=source['password'])

    model = conn.model('account.invoice.line')
    rec_ids = model.search([('account_id.fiscal_type_id','=',4)])

    datas =  model.export_data(rec_ids, ['.id','id/id', 'name'])['datas']
    for data in datas:
        print(data)


get_source_data()
