# Script para mapear las provincias entre odoo V8 y odoo V13
############################################################

# Odoo V13
##########
#	Ciudad Autónoma de Buenos Aires	---	base.state_ar_c
#	Salta	                        ---	base.state_ar_a
#	Buenos Aires	                ---	base.state_ar_b
#	San Luis	                    ---	base.state_ar_d
#	Entre Ríos	                    ---	base.state_ar_e
#	La Rioja	                    ---	base.state_ar_f
#	Santiago Del Estero	            ---	base.state_ar_g
#	Chaco	                        ---	base.state_ar_h
#	San Juan	        ---	base.state_ar_j
#	Catamarca	        ---	base.state_ar_k
#	La Pampa	        ---	base.state_ar_l
#	Mendoza	            ---	base.state_ar_m
#	Misiones	        ---	base.state_ar_n
#	Formosa	            ---	base.state_ar_p
#	Neuquén	            ---	base.state_ar_q
#	Río Negro   	    ---	base.state_ar_r
#	Santa Fe	        ---	base.state_ar_s
#	Tucumán   	        ---	base.state_ar_t
#	Chubut	            ---	base.state_ar_u
#	Tierra del Fuego  	---	base.state_ar_v
#	Corrientes	        ---	base.state_ar_w
#	Córdoba	            ---	base.state_ar_x
#	Jujuy	            ---	base.state_ar_y
#	Santa Cruz	        ---	base.state_ar_z

# Odoo V8
##########
#	Ciudad Autonoma de Buenos Aires 	l10n_ar_base_country_state.state_capital_federal
#	Buenos Aires 	    l10n_ar_base_country_state.state_buenos_aires
#	CABA 	    __export__.res_country_state_117
#	Catamarca 	    l10n_ar_base_country_state.state_catamarca
#	Catamarca 	    l10n_ar_states.K
#	Chaco 	    l10n_ar_base_country_state.state_chaco
#	Chaco 	    l10n_ar_states.H
#	Chubut 	    l10n_ar_base_country_state.state_chubut
#	Chubut 	    l10n_ar_states.U
#	Cordoba 	    l10n_ar_base_country_state.state_cordoba
#	Córdoba 	    l10n_ar_states.X
#	Corrientes 	    l10n_ar_base_country_state.state_corrientes
#	Corrientes 	    l10n_ar_states.W
#	Entre Ríos 	    l10n_ar_base_country_state.state_entre_rios
#	Entre Ríos 	    l10n_ar_states.E
#	Formosa 	    l10n_ar_base_country_state.state_formosa
#	Formosa 	    l10n_ar_states.P
#	Jujuy 	    l10n_ar_base_country_state.state_jujuy
#	Jujuy 	    l10n_ar_states.Y
#	La Pampa 	    l10n_ar_base_country_state.state_la_pampa
#	La Pampa 	    l10n_ar_states.L
#	La Rioja 	    l10n_ar_base_country_state.state_la_rioja
#	La Rioja 	    l10n_ar_states.F
#	Mendoza 	    l10n_ar_base_country_state.state_mendoza
#	Mendoza 	    l10n_ar_states.M
#	Misiones 	    l10n_ar_base_country_state.state_misiones
#	Misiones 	    l10n_ar_states.N
#	Neuquén 	    l10n_ar_base_country_state.state_neuquen
#	Neuquén 	    l10n_ar_states.Q
#	Rio Negro 	    __export__.res_country_state_86
#	Río Negro 	    l10n_ar_base_country_state.state_rio_negro
#	Río Negro 	    l10n_ar_states.R
#	Salta 	    l10n_ar_base_country_state.state_salta
#	Salta 	    l10n_ar_states.A
#	San Juan 	    l10n_ar_base_country_state.state_san_juan
#	San Juan 	    l10n_ar_states.J
#	San Luis 	    l10n_ar_base_country_state.state_san_luis
#	San Luis 	    l10n_ar_states.D
#	Santa Cruz 	    l10n_ar_base_country_state.state_santa_cruz
#	Santa Cruz 	    l10n_ar_states.Z
#	Santa Fe 	    l10n_ar_base_country_state.state_santa_fe
#	Santa Fe 	    l10n_ar_states.S
#	Santa Fe  	    __export__.res_country_state_84
#	Santiago del Estero 	    l10n_ar_base_country_state.state_sgo_del_estero
#	Santiago del Estero 	    l10n_ar_states.G
#	Tierra del Fuego	l10n_ar_base_country_state.state_tierra_del_fuego
#	Tierra del Fuego 	    l10n_ar_states.V
#	Tucumán 	    l10n_ar_base_country_state.state_tucuman
#	Tucumán 	    l10n_ar_states.T
#	Villa sarmiento 	    __export__.res_country_state_127


def map_city(source):
  """ Mapea un identificador externo del modelo res.country.state de v8 a v13
      Notar que en algunos casos en v8 esta duplicada la provincia,
      Caso de Tucuman o Misiones
  """
  # Buenos Aires y todos los extranjeros.
  if (source == 'l10n_ar_base_country_state.state_buenos_aires' or source == '__export__.res_country_state_127' or
      source == '__export__.res_country_state_122' or source == 'state_us_45' or source == '__export__.res_country_state_127' or
      source == '__export__.state_us_45'):
    return 'base.state_ar_b'


  # Ciudad Autónoma de Buenos Aires o CABA
  if source == 'l10n_ar_base_country_state.state_capital_federal' or source =='__export__.res_country_state_117':
    return 'base.state_ar_c'
  # Salta
  if source == 'l10n_ar_base_country_state.state_salta' or source == 'l10n_ar_states.A':
    return 'base.state_ar_a'
  # San Luis
  if source == 'l10n_ar_base_country_state.state_san_luis' or source == 'l10n_ar_states.D':
    return 'base.state_ar_d'
  # Entre Rios
  if source == 'l10n_ar_base_country_state.state_entre_rios' or source == 'l10n_ar_states.E':
    return 'base.state_ar_e'
  # La Rioja
  if source == 'l10n_ar_base_country_state.state_la_rioja' or source ==  'l10n_ar_states.F':
    return 'base.state_ar_f'
  # Santiago Del Estero
  if source == 'l10n_ar_base_country_state.state_la_rioja' or source == 'l10n_ar_states.F':
    return 'base.state_ar_g'
  # Chaco
  if source == 'l10n_ar_base_country_state.state_chaco' or source == 'l10n_ar_states.H':
    return 'base.state_ar_h'
  # San Juan
  if source == 'l10n_ar_base_country_state.state_san_juan' or source == 'l10n_ar_states.J':
    return 'base.state_ar_j'
  # Catamarca
  if source == 'l10n_ar_base_country_state.state_catamarca' or source == 'l10n_ar_states.K':
    return 'base.state_ar_k'
  # La Pampa
  if source == 'l10n_ar_base_country_state.state_la_pampa' or source == 'l10n_ar_states.L':
    return 'base.state_ar_l'
  # Mendoza
  if source == 'l10n_ar_base_country_state.state_mendoza' or  source == 'l10n_ar_states.M':
    return 'base.state_ar_m'
  # Misiones
  if source == 'l10n_ar_base_country_state.state_misiones' or source == 'l10n_ar_states.N':
    return 'base.state_ar_n'
  # Formosa
  if source == 'l10n_ar_base_country_state.state_formosa' or source == 'l10n_ar_states.P':
    return 'base.state_ar_p'
  # Neuquén
  if source == 'l10n_ar_base_country_state.state_neuquen' or source == 'l10n_ar_states.Q':
    return 'base.state_ar_q'
  # Río Negro
  if source == '__export__.res_country_state_86' or source == 'l10n_ar_base_country_state.state_rio_negro' or source =='l10n_ar_states.R':
    return 'base.state_ar_r'
  # Santa Fe
  if source == 'l10n_ar_base_country_state.state_santa_fe' or source == 'l10n_ar_states.S' or source == '__export__.res_country_state_84':
    return 'base.state_ar_s'
  # Tucuman
  if source == 'l10n_ar_base_country_state.state_tucuman' or source == 'l10n_ar_states.T':
    return 'base.state_ar_t'
  # Chubut
  if source == 'l10n_ar_base_country_state.state_chubut' or source == 'l10n_ar_states.U':
    return 'base.state_ar_u'
  # Tierra del Fuego
  if source == 'l10n_ar_base_country_state.state_tierra_del_fuego' or  source == 'l10n_ar_states.V':
    return 'base.state_ar_v'
  # Corrientes
  if source == 'l10n_ar_base_country_state.state_corrientes' or source == 'l10n_ar_states.W':
    return 'base.state_ar_w'
  # Córdoba
  if source == 'l10n_ar_base_country_state.state_cordoba' or source == 'l10n_ar_states.X':
    return 'base.state_ar_x'
  # Jujuy
  if source == 'l10n_ar_base_country_state.state_jujuy' or source == 'l10n_ar_states.Y':
    return 'base.state_ar_y'
  # Santa Cruz
  if source == 'l10n_ar_base_country_state.state_santa_cruz' or source == 'l10n_ar_states.Z':
    return 'base.state_ar_z'

  # ninguno de los anteriores
  #raise Exception('Identificador externo no encontrado en migration script. %s' % source)
  return 'base.state_ar_b'

# obtener el identificador externo en source
model = source_connection.model('res.partner')
source_external_id = model.export_data([rec_id], ['state_id/id'])['datas'][0][0]

# mapear identificador externo de source a target y devolverlo
context['result'] = map_city(source_external_id) if source_external_id else False
