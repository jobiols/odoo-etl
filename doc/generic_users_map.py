# Script para mapear los usuarios odoo V8 y odoo V13
############################################################

# Odoo V13
##########

# Odoo V8
##########
#	__export__.res_users_70	---	ABRE INTEGRADORES
#	base.user_root	---	Administrator
#	__export__.res_users_5	---	Agustina Mancini
#	__export__.res_users_63	---	Alejandra Parada
#	__export__.res_users_78	---	Alejandro Romano
#	__export__.res_users_6	---	Angel Reale
#	__export__.res_users_23	---	Ayelen Debuglio
#	__export__.res_users_8	---	Daniel Giovagnoni
#	__export__.res_users_60	---	Fernando Saljayi
#	__export__.res_users_71	---	Gabriela Leinhold
#	__export__.res_users_61	---	Gaston Picon
#	__export__.res_users_24	---	Lucas Limeres
#	__export__.res_users_68	---	Maria Belen Mansilla
#	__export__.res_users_37	---	Mariano Juarez
#	__export__.res_users_73	---	Mariela Perez Gonzalez
#	__export__.res_users_12	---	Maximiliano Gimenez
#	__export__.res_users_76	---	Mili
#	__export__.res_users_50	---	Natalia Sommariva
#	__export__.res_users_47	---	Norman Widd
#	__export__.res_users_75	---	Pau
#	__export__.res_users_36	---	Prueba
#	__export__.res_users_80	---	Quilsoft
#	__export__.res_users_74	---	Roberto Valenta
#	__export__.res_users_72	---	Rosa Perin
#	__export__.res_users_32	---	Santiago Arroyo
#	__export__.res_users_15	---	Sergio Oroña
#	__export__.res_users_67	---	Tercerizate


MODEL = 'res.partner'

def map_users(source):
  """ Mapea un identificador externo del modelo res.user de v8 a v13
  """

  # ninguno de los anteriores
  raise Exception('Identificador externo no encontrado. %s' % source)

# obtener el identificador externo en source
model = source_connection.model(MODEL)
source_external_id = model.export_data([rec_id], ['state_id/id'])['datas'][0][0]

# mapear identificador externo de source a target y devolverlo
context['result'] = map_city(source_external_id) if source_external_id else False
