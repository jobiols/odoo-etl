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

def _get_target():
    conn = Client(target['host'], db=target['db'], user=target['user'], password=target['password'])
    model = conn.model('account.move')
    ids = model.search([])
    datas = model.export_data(rec_ids, ['account_id/id'])['datas']

    datas = model.execute('action_post')

def get_source_data():
    conn = Client(source['host'], db=source['db'], user=source['user'], password=source['password'])

    model = conn.model('account.invoice')
    rec_ids = model.search([('id', '>=', 15000),
                            ('id', '<',  1600000)])
    print(len(rec_ids))

    return model.export_data(rec_ids, ['id/id', 'state'])['datas']


def post_invoices():
    conn = Client(target['host'], db=target['db'], user=target['user'], password=target['password'])

    # Draft, Pro-forma, Open, Paid, Cancelled
    duplicates = []
    datas = get_source_data()
    for data in datas:
        print(data)
        ret = conn.execute('account.move', 'post_invoices', 1, {'param': data})
        print(ret)
        if not ret['ok']:
            duplicates.append([ret.get('invoice'),ret.get('date'), ret.get('msg')])
            print(ret.get('invoice'), ret.get('date'), ret.get('msg'))

    import csv
    with open('errores.csv', mode='a') as file:
        writer = csv.writer(file)
        for line in duplicates:
            writer.writerow(line)

post_invoices()
