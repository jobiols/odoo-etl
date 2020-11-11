# Script para mapear posiciones fiscales entre odoo V8 y odoo V13
#################################################################

# Odoo v13
#####################################
#  res_IVARI      --- IVA Responsable Inscripto
#  res_IVARNI     --- IVA Responsable no Inscripto
#  res_IVANR IVA  --- no Responsable
#  res_IVAE IVA   --- Sujeto Exento
#  res_CF         --- Consumidor Final
#  res_RM         --- Responsable Monotributo
#  res_NOCATEG    --- Sujeto no Categorizado
#  res_EXT        --- Cliente / Proveedor del Exterior
#  res_IVA_LIB    --- IVA Liberado – Ley Nº 19.640
#  res_IVARI_AP   --- IVA Responsable Inscripto – Agente de Percepción
#  res_EVENTUAL   --- Pequeño Contribuyente Eventual
#  res_MON_SOCIAL       --- Monotributista Social
#  res_EVENTUAL_SOCIAL  --- Pequeño Contribuyente Eventual Social

# Odoo V8
#####################################
# Responsable Inscripto	--- l10n_ar_point_of_sale.fiscal_position_ri
# Consumidor final	    --- l10n_ar_point_of_sale.fiscal_position_final_cons
# Exento	              --- l10n_ar_point_of_sale.fiscal_position_exempt
# Exterior              ---	__export__.account_fiscal_position_5
# Monotributo           ---	l10n_ar_point_of_sale.fiscal_position_mono
# RI M	                --- __export__.account_fiscal_position_6
# RI OC	                --- __export__.account_fiscal_position_8
# RI X	                --- __export__.account_fiscal_position_7

def map_responsability(source):
  """ Mapea un identificador externo de v8 a v13
  """
  # Responsable Inscripto
  if source == 'l10n_ar_point_of_sale.fiscal_position_ri':
    return 'l10n_ar.res_IVARI'

  # Consumidor final
  if source == 'l10n_ar_point_of_sale.fiscal_position_final_cons':
    return 'l10n_ar.res_CF'

  # Exento
  if source == 'l10n_ar_point_of_sale.fiscal_position_exempt':
    return 'l10n_ar.res_IVAE'

  # Exterior
  if source == '__export__.account_fiscal_position_5':
    return 'l10n_ar.res_EXT'

  # Monotributo
  if source == 'l10n_ar_point_of_sale.fiscal_position_mono':
    return 'l10n_ar.res_RM'

  # ninguno de los anteriores
  raise Exception('Identificador externo no encontrado en migration script. %s' % source)

# obtener el identificador externo en source
model = source_connection.model('res.partner')
source_external_id = model.export_data([rec_id], ['property_account_position/id'])['datas'][0][0]

# mapear identificador externo de source a target y devolverlo
context['result'] = map_responsability(source_external_id) if source_external_id else False
