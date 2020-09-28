
# export_data no funciona y no sabemos que devolvia
# usamos esto

source_model_obj.browse([1, 2, 3]).read(['street'])

[
    {'id': 1, 'street': ''},
    {'id': 2, 'street': False},
    {'id': 3, 'street': False}
]
