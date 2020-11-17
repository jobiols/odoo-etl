# Script para mapear impuestos entre odoo V8 y odoo V13
#################################################################

# Odoo v13
#####################################
#  ri_tax_percepcion_iva_aplicada
#  ri_tax_percepcion_ganancias_aplicada
#  ri_tax_percepcion_ganancias_sufrida
#  ri_tax_percepcion_iibb_caba_sufrida
#  ri_tax_percepcion_iibb_ba_sufrida  --  buenos aires
#  ri_tax_percepcion_iibb_co_sufrida  --  cordoba
#  ri_tax_percepcion_iibb_sf_sufrida  --  santa fe
#  ri_tax_percepcion_iibb_aplicada
#  ri_tax_vat_no_corresponde_ventas
#  ri_tax_vat_no_corresponde_compras
#  ri_tax_vat_no_gravado_ventas
#  ri_tax_vat_no_gravado_compras
#  ri_tax_vat_exento_ventas
#  ri_tax_vat_exento_compras
#  ri_tax_vat_0_ventas
#  ri_tax_vat_0_compras
#  ri_tax_vat_10_ventas
#  ri_tax_vat_10_compras
#  ri_tax_vat_21_ventas
#  ri_tax_vat_21_compras
#  ri_tax_vat_27_ventas
#  ri_tax_vat_27_compras
#  ri_tax_vat_25_ventas
#  ri_tax_vat_25_compras
#  ri_tax_vat_5_ventas
#  ri_tax_vat_5_compras
#  ri_tax_percepcion_iva_sufrida
#  ri_tax_ganancias_iva_adicional

# Odoo V8
#####################################
#	account_base_config.account_tax_301	---	IVA	IVA COMPRAS EXENTO
#	account_base_config.account_tax_299	---	IVA	IVA COMPRAS 27%
#	account_base_config.account_tax_004	---	IVA	IVA VENTAS 10.5%
#	__export__.account_tax_746	---	Retención	Retencion de TISSH
#	__export__.account_tax_745	---	IVA	21
#	__export__.account_tax_784	---	IVA	10.5}
#	account_base_config.account_tax_006	---	IVA	IVA COMPRAS 10.5%
#	account_base_config.account_tax_003	---	IVA	IVA VENTAS EXENTO
#	__export__.account_tax_782	---	Otro	Fondo De Financiamiento de Servicios Sociales
#	__export__.account_tax_775	---	IVA	iva c
#	__export__.account_tax_760	---	IVA	1355
#	__export__.account_tax_767	---	IVA	10.5
#	__export__.account_tax_774	---	IVA	IVA}
#	__export__.account_tax_747	---	IVA	10
#	__export__.account_tax_773	---	IVA	IVA 10
#	__export__.account_tax_770	---	IVA	iova
#	__export__.account_tax_739	---	IVA	IVA VENTAS 21%
#	account_base_config.account_tax_005	---	IVA	IVA COMPRAS 21%
#	account_base_config.account_tax_300	---	IVA	IVA COMPRAS ND
#	__export__.account_tax_749	---	IVA	27
#	__export__.account_tax_756	---	IVA	FINANCIAMIENTO ERAS
#	l10n_ar_perceptions_basic.tax_percepcion_iva_sufrida	---	Percepción	Percepciones IVA sufrida
#	l10n_ar_retentions_basic.tax_retencion_iva_sufrida	---	Retención	Retencion IVA Sufrida
#	l10n_ar_retentions_basic.tax_retencion_iva_efectuada	---	Retención	Retencion IVA Efectuada
#	account_base_config.account_tax_281	---	Retención	Retenciones IIBB CORRIENTES sufrida
#	account_base_config.account_tax_244	---	Percepción	Percepciones IIBB RIO NEGRO sufrida
#	account_base_config.account_tax_255	---	Retención	Retenciones IIBB CHACO efectuada
#	account_base_config.account_tax_291	---	Retención	Retenciones IIBB SALTA sufrida
#	account_base_config.account_tax_290	---	Retención	Retenciones IIBB RIO NEGRO sufrida
#	account_base_config.account_tax_277	---	Retención	Retenciones IIBB CATAMARCA sufrida
#	account_base_config.account_tax_278	---	Retención	Retenciones IIBB CHACO sufrida
#	account_base_config.account_tax_279	---	Retención	Retenciones IIBB CHUBUT sufrida
#	account_base_config.account_tax_231	---	Percepción	Percepciones IIBB CATAMARCA sufrida
#	account_base_config.account_tax_280	---	Retención	Retenciones IIBB CORDOBA sufrida
#	account_base_config.account_tax_021	---	Retención	Retencion IIBB ARBA Sufrida
#	account_base_config.account_tax_283	---	Retención	Retenciones IIBB FORMOSA sufrida
#	account_base_config.account_tax_284	---	Retención	Retenciones IIBB JUJUY sufrida
#	account_base_config.account_tax_285	---	Retención	Retenciones IIBB LA PAMPA sufrida
#	account_base_config.account_tax_286	---	Retención	Retenciones IIBB LA RIOJA sufrida
#	account_base_config.account_tax_292	---	Retención	Retenciones IIBB SAN JUAN sufrida
#	account_base_config.account_tax_294	---	Retención	Retenciones IIBB SANTA CRUZ sufrida
#	account_base_config.account_tax_296	---	Retención	Retenciones IIBB SANTIAGO DEL ESTERO sufrida
#	account_base_config.account_tax_287	---	Retención	Retenciones IIBB MENDOZA sufrida
#	account_base_config.account_tax_295	---	Retención	Retenciones IIBB SANTA FE sufrida
#	account_base_config.account_tax_293	---	Retención	Retenciones IIBB SAN LUIS sufrida
#	account_base_config.account_tax_288	---	Retención	Retenciones IIBB MISIONES sufrida
#	account_base_config.account_tax_282	---	Retención	Retenciones IIBB ENTRE RIOS sufrida
#	l10n_ar_retentions_basic.tax_retencion_iibb_caba_sufrida	---	Retención	Retencion IIBB CABA Sufrida
#	account_base_config.account_tax_249	---	Percepción	Percepciones IIBB SANTA FE sufrida
#	account_base_config.account_tax_250	---	Percepción	Percepciones IIBB SANTIAGO DEL ESTERO sufrida
#	l10n_ar_retentions_basic.tax_retencion_iibb_caba_efectuada	---	Retención	Retencion IIBB CABA Efectuada
#	l10n_ar_perceptions_basic.tax_percepcion_iibb_caba_sufrida	---	Percepción	Percepciones IIBB CABA sufrida
#	l10n_ar_perceptions_basic.tax_percepcion_iva_efectuada	---	Percepción	Percepciones IVA efectuada
#	account_base_config.account_tax_251	---	Percepción	Percepciones IIBB TIERRA DEL FUEGO sufrida
#	account_base_config.account_tax_232	---	Percepción	Percepciones IIBB CHACO sufrida
#	account_base_config.account_tax_236	---	Percepción	Percepciones IIBB ENTRE RIOS sufrida
#	account_base_config.account_tax_237	---	Percepción	Percepciones IIBB FORMOSA sufrida
#	account_base_config.account_tax_238	---	Percepción	Percepciones IIBB JUJUY sufrida
#	account_base_config.account_tax_239	---	Percepción	Percepciones IIBB LA PAMPA sufrida
#	account_base_config.account_tax_240	---	Percepción	Percepciones IIBB LA RIOJA sufrida
#	account_base_config.account_tax_289	---	Retención	Retenciones IIBB NEUQUEN sufrida
#	account_base_config.account_tax_297	---	Retención	Retenciones IIBB TIERRA DEL FUEGO sufrida
#	account_base_config.account_tax_298	---	Retención	Retenciones IIBB TUCUMAN sufrida
#	account_base_config.account_tax_019	---	Percepción	Percepciones IIBB ARBA sufrida
#	account_base_config.account_tax_233	---	Percepción	Percepciones IIBB CHUBUT sufrida
#	account_base_config.account_tax_234	---	Percepción	Percepciones IIBB CORDOBA sufrida
#	account_base_config.account_tax_235	---	Percepción	Percepciones IIBB CORRIENTES sufrida
#	account_base_config.account_tax_241	---	Percepción	Percepciones IIBB MENDOZA sufrida
#	account_base_config.account_tax_242	---	Percepción	Percepciones IIBB MISIONES sufrida
#	account_base_config.account_tax_243	---	Percepción	Percepciones IIBB NEUQUEN sufrida
#	account_base_config.account_tax_245	---	Percepción	Percepciones IIBB SALTA sufrida
#	account_base_config.account_tax_246	---	Percepción	Percepciones IIBB SAN JUAN sufrida
#	account_base_config.account_tax_247	---	Percepción	Percepciones IIBB SAN LUIS sufrida
#	account_base_config.account_tax_248	---	Percepción	Percepciones IIBB SANTA CRUZ sufrida
#	account_base_config.account_tax_020	---	Retención	Retencion IIBB ARBA Efectuada
#	account_base_config.account_tax_252	---	Percepción	Percepciones IIBB TUCUMAN sufrida
#	account_base_config.account_tax_254	---	Retención	Retenciones IIBB CATAMARCA efectuada
#	account_base_config.account_tax_256	---	Retención	Retenciones IIBB CHUBUT efectuada
#	account_base_config.account_tax_257	---	Retención	Retenciones IIBB CORDOBA efectuada
#	account_base_config.account_tax_258	---	Retención	Retenciones IIBB CORRIENTES efectuada
#	account_base_config.account_tax_259	---	Retención	Retenciones IIBB ENTRE RIOS efectuada
#	account_base_config.account_tax_260	---	Retención	Retenciones IIBB FORMOSA efectuada
#	account_base_config.account_tax_261	---	Retención	Retenciones IIBB JUJUY efectuada
#	account_base_config.account_tax_262	---	Retención	Retenciones IIBB LA PAMPA efectuada
#	account_base_config.account_tax_263	---	Retención	Retenciones IIBB LA RIOJA efectuada
#	account_base_config.account_tax_264	---	Retención	Retenciones IIBB MENDOZA efectuada
#	account_base_config.account_tax_265	---	Retención	Retenciones IIBB MISIONES efectuada
#	account_base_config.account_tax_266	---	Retención	Retenciones IIBB NEUQUEN efectuada
#	account_base_config.account_tax_267	---	Retención	Retenciones IIBB RIO NEGRO efectuada
#	account_base_config.account_tax_268	---	Retención	Retenciones IIBB SALTA efectuada
#	account_base_config.account_tax_269	---	Retención	Retenciones IIBB SAN JUAN efectuada
#	account_base_config.account_tax_270	---	Retención	Retenciones IIBB SAN LUIS efectuada
#	account_base_config.account_tax_271	---	Retención	Retenciones IIBB SANTA CRUZ efectuada
#	account_base_config.account_tax_272	---	Retención	Retenciones IIBB SANTA FE efectuada
#	account_base_config.account_tax_273	---	Retención	Retenciones IIBB SANTIAGO DEL ESTERO efectuada
#	account_base_config.account_tax_274	---	Retención	Retenciones IIBB TIERRA DEL FUEGO efectuada
#	account_base_config.account_tax_275	---	Retención	Retenciones IIBB TUCUMAN efectuada
#	account_base_config.account_tax_212	---	Percepción	Percepciones IIBB CORRIENTES efectuada
#	account_base_config.account_tax_224	---	Percepción	Percepciones IIBB SAN LUIS efectuada
#	account_base_config.account_tax_229	---	Percepción	Percepciones IIBB TUCUMAN efectuada
#	account_base_config.account_tax_213	---	Percepción	Percepciones IIBB ENTRE RIOS efectuada
#	account_base_config.account_tax_214	---	Percepción	Percepciones IIBB FORMOSA efectuada
#	account_base_config.account_tax_227	---	Percepción	Percepciones IIBB SANTIAGO DEL ESTERO efectuada
#	account_base_config.account_tax_225	---	Percepción	Percepciones IIBB SANTA CRUZ efectuada
#	account_base_config.account_tax_228	---	Percepción	Percepciones IIBB TIERRA DEL FUEGO efectuada
#	account_base_config.account_tax_208	---	Percepción	Percepciones IIBB CATAMARCA efectuada
#	account_base_config.account_tax_209	---	Percepción	Percepciones IIBB CHACO efectuada
#	account_base_config.account_tax_210	---	Percepción	Percepciones IIBB CHUBUT efectuada
#	account_base_config.account_tax_226	---	Percepción	Percepciones IIBB SANTA FE efectuada
#	account_base_config.account_tax_211	---	Percepción	Percepciones IIBB CORDOBA efectuada
#	account_base_config.account_tax_223	---	Percepción	Percepciones IIBB SAN JUAN efectuada
#	account_base_config.account_tax_222	---	Percepción	Percepciones IIBB SALTA efectuada
#	account_base_config.account_tax_218	---	Percepción	Percepciones IIBB MENDOZA efectuada
#	account_base_config.account_tax_221	---	Percepción	Percepciones IIBB RIO NEGRO efectuada
#	l10n_ar_perceptions_basic.tax_percepcion_iibb_caba_efectuada	---	Percepción	Percepciones IIBB CABA efectuada
#	account_base_config.account_tax_220	---	Percepción	Percepciones IIBB NEUQUEN efectuada
#	account_base_config.account_tax_217	---	Percepción	Percepciones IIBB LA RIOJA efectuada
#	account_base_config.account_tax_219	---	Percepción	Percepciones IIBB MISIONES efectuada
#	account_base_config.account_tax_216	---	Percepción	Percepciones IIBB LA PAMPA efectuada
#	account_base_config.account_tax_215	---	Percepción	Percepciones IIBB JUJUY efectuada
#	account_base_config.account_tax_022	---	Percepción	Percepciones IIBB ARBA efectuada
#	l10n_ar_retentions_basic.tax_retencion_ganancias_sufrida	---	Retención	Retencion Ganancias Sufrida
#	l10n_ar_retentions_basic.tax_retencion_suss_sufrida	---	Retención	Retencion SUSS Sufrida
#	l10n_ar_retentions_basic.tax_retencion_ganancias_efectuada	---	Retención	Retenciones Ganancias Efectuada
#	l10n_ar_retentions_basic.tax_retencion_suss_efectuada	---	Retención	Retenciones SUSS Efectuada

def map_tax(source):
  """ Mapea un impuesto en una linea de factura de v8 a v13
  """
  # IVA Compras 21%
  if source == 'ri_tax_vat_21_compras':
    return 'account_base_config.account_tax_005'
  if source == 'ri_tax_vat_21_compras':
    return '__export.account_tax_745'
  # IVA Ventas 21%
  if source == 'ri_tax_vat_21_ventas':
    return '__export__.account_tax_739'
  if source == 'ri_tax_vat_21_ventas':
    return '__export.account_tax_745'
  # IVA Compras 10.5%
  if source == 'ri_tax_vat_10_compras':
    return 'account_base_config.account_tax_006'
  if source == 'ri_tax_vat_10_compras':
    return '__export.account_tax_784'
  if source == 'ri_tax_vat_10_compras':
    return '__export__.account_tax_767'
  # IVA Ventas 10.5%
  if source == 'ri_tax_vat_10_ventas':
    return 'account_base_config.account_tax_004'
  if source == 'ri_tax_vat_10_ventas':
    return '__export.account_tax_784'
  if source == 'ri_tax_vat_10_ventas':
    return '__export__.account_tax_767'
  # Retencion de TISSH
  if source == 'ri_tax_retencion_tissh':
    return '__export.account_tax_746'
  # Percepción IVA aplicada
  if source == 'ri_tax_percepcion_iva_aplicada':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iva_efectuada'
  # Fondo de financiamiento de servicios sociales
  if source == 'ri_tax_fondo_ss':
    return '__export.account_tax_782'
  # Percepción ganancias aplicada. No se encontró en V8

  # Percepción ganancias sufrida. No se encontró en V8

  # Percepción IIBB CABA sufrida
  if source == 'ri_tax_percepcion_iibb_caba_sufrida':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iibb_caba_sufrida'
  # Percepción IIBB ARBA sufrida
  if source == 'ri_tax_percepcion_iibb_arba_sufrida':
    return 'account_base_config.account_tax_019'
  # Percepción IIBB CORDOBA sufrida
  if source == 'ri_tax_percepcion_iibb_cordoba_sufrida':
    return 'account_base_config.account_tax_234'
  # Percepción IIBB Santa Fe
  if source == 'ri_tax_percepcion_iibb_santafe_sufrida':
    return 'account_base_config.account_tax_249'
  # Percepción IIBB CABA aplicada
  if source == 'ri_tax_percepcion_iibb_aplicada':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iibb_caba_efectuada'

  # IVA No Corresponde Ventas. No se encontró en V8
  #ID ri_tax_percepcion_iva_aplicada

  # IVA No Corresponde Compras. No se encontró en V8
  #ID ri_tax_percepcion_ganancias_sufrida

  # IVA No Gravado Ventas. No se encontró en V8
  #ID ri_tax_vat_no_gravado_ventas

  # IVA No Gravado Compras. No se encontró en V8
  #ID ri_tax_vat_no_gravado_compras

  # IVA Exento Ventas
  if source == 'ri_tax_vat_exento_ventas':
    return 'account_base_config.account_tax_003'
  # IVA Exento Compras
  if source == 'ri_tax_vat_exento_compras':
    return 'account_base_config.account_tax_301'
  # IVA Ventas 0
  if source == 'ri_tax_percepcion_iva_aplicada':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iva_efectuada'
  # IVA Ventas 0.
  if source == 'ri_tax_percepcion_iva_aplicada':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iva_efectuada'
  # IVA Ventas 0
  if source == 'ri_tax_percepcion_iva_aplicada':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iva_efectuada'

  # IVA Ventas 0. No se encontró en V8
#  ID ri_tax_vat_0_ventas
  # IVA Compras 0. No se encontró en V8
#  ID ri_tax_vat_0_compras

  # IVA Ventas 10
  if source == 'ri_tax_vat_10_ventas':
    return '__export__.account_tax_747'
  if source == 'ri_tax_vat_10_ventas':
    return '__export__.account_tax_773'
  # IVA Compras 10
  if source == 'ri_tax_vat_10_compras':
    return '__export__.account_tax_747'
  if source == 'ri_tax_vat_10_compras':
    return '__export__.account_tax_773'
  # IVA Ventas 21
  if source == 'ri_tax_vat_21_ventas':
    return '__export__.account_tax_739'
  # IVA Compras 21
  if source == 'ri_tax_vat_21_compras':
    return 'account_base_config.account_tax_005'
  # IVA Ventas 27
  if source == 'ri_tax_vat_27_ventas':
    return '__export__.account_tax_749'
  # IVA Compras 27
  if source == 'ri_tax_vat_27_compras':
    return '__export__.account_tax_749'
  if source == 'ri_tax_vat_27_compras':
    return 'account_base_config.account_tax_299'

  # IVA Ventas 25. No se encontró en V8
#  ID ri_tax_vat_25_ventas

  # IVA Compras 25. No se encontró en V8
#  ID ri_tax_vat_25_compras

  # IVA Ventas 5. No se encontró en V8
#  ID ri_tax_vat_5_ventas

  # IVA Compras 5. No se encontró en V8
#  ID ri_tax_vat_5_compras

  # IVA Percepción IVA Sufrida
  if source == 'ri_tax_percepcion_iva_sufrida':
    return 'l10n_ar_perceptions_basic.tax_percepcion_iva_sufrida'

  # IVA Compras ND
  if source == 'ri_tax_compras_nd':
    return 'account_base_config.account_tax_300'

  # IVA Ganancias Adicional. No se encontró en v8
#  ID ri_tax_ganancias_iva_adicional

  # Retención IVA Sufrida
  if source == 'ri_tax_retencion_iva_sufrida':
    return 'l10n_ar_retentions_basic.tax_retencion_iva_sufrida'

  # Retención IVA efectuada
  if source == 'ri_tax_retencion_iva_efectuada':
    return 'l10n_ar_retentions_basic.tax_retencion_iva_efectuada'

  # Retención IIBB Rio Negro Efectuada
  if source == 'ri_tax_retencion_iibb_rionegro_efectuada':
    return 'account_base_config.account_tax_221'
  # Percepción IIBB Neuquen Sufrida
  if source == 'ri_tax_percepcion_iibb_neuquen_sufrida':
    return 'account_base_config.account_tax_243'
  # Percepción IIBB San Juan Sufrida
  if source == 'ri_tax_percepcion_iibb_sanjuan_sufrida':
    return 'account_base_config.account_tax_246'
  # Percepción IIBB San Luis Sufrida
  if source == 'ri_tax_percepcion_iibb_sanluis_sufrida':
    return 'account_base_config.account_tax_247'
  # Percepción IIBB Santa Cruz Sufrida
  if source == 'ri_tax_percepcion_iibb_santacruz_sufrida':
    return 'account_base_config.account_tax_248'
  # Retención IIBB ARBA Efectuada
  if source == 'ri_tax_retencion_iibb_arba_efectuada':
    return 'account_base_config.account_tax_020'
  # Percepción IIBB Tucuman Sufrida
  if source == 'ri_tax_percepcion_iibb_tucuman_sufrida':
    return 'account_base_config.account_tax_252'
  # Retención IIBB Catamarca Efectuada
  if source == 'ri_tax_retencion_iibb_catamarca_efectuada':
    return 'account_base_config.account_tax_254'
  # Retención IIBB Chubut Efectuada
  if source == 'ri_tax_retencion_iibb_chubut_efectuada':
    return 'account_base_config.account_tax_256'
  # Retención IIBB Córdoba Efectuada
  if source == 'ri_tax_retencion_iibb_cordoba_efectuada':
    return 'account_base_config.account_tax_257'
  # Retención IIBB Corrientes Efectuada
  if source == 'ri_tax_retencion_iibb_entrerios_efectuada':
    return 'account_base_config.account_tax_258'
  # Retención IIBB Entre Ríos Efectuada
  if source == 'ri_tax_retencion_iibb_entrerios_efectuada':
    return 'account_base_config.account_tax_259'
  # Retención IIBB Formosa Efectuada
  if source == 'ri_tax_retencion_iibb_formosa_efectuada':
    return 'account_base_config.account_tax_260'
  # Retención IIBB Jujuy Efectuada
  if source == 'ri_tax_retencion_iibb_jujuy_efectuada':
    return 'account_base_config.account_tax_261'
    # Retención IIBB La Pampa Efectuada
  if source == 'ri_tax_retencion_iibb_lapampa_efectuada':
    return 'account_base_config.account_tax_262'
  # Retención IIBB La Rioja Efectuada
  if source == 'ri_tax_vat_27_compras':
    return 'account_base_config.account_tax_263'
  # Retención IIBB Mendoza Efectuada
  if source == 'ri_tax_retencion_iibb_mendoza_efectuada':
    return 'account_base_config.account_tax_264'
  # Retención IIBB Misiones Efectuada
  if source == 'ri_tax_retencion_iibb_misiones_efectuada':
    return 'account_base_config.account_tax_265'
  # Retención IIBB Neuquen Efectuada
  if source == 'ri_tax_retencion_iibb_neuquen_efectuada':
    return 'account_base_config.account_tax_266'
  # Retención IIBB Río Negro Efectuada
  if source == 'ri_tax_retencion_iibb_rionegro_efectuada':
    return 'account_base_config.account_tax_267'
  # Retención IIBB Salta Efectuada
  if source == 'ri_tax_retencion_iibb_salta_efectuada':
    return 'account_base_config.account_tax_268'
  # Retención IIBB San Juan Efectuada
  if source == 'ri_tax_retencion_iibb_sanjuan_efectuada':
    return 'account_base_config.account_tax_269'
  # Retención IIBB San Luis Efectuada
  if source == 'ri_tax_retencion_iibb_sanluis_efectuada':
    return 'account_base_config.account_tax_270'
  # Retención Santa Cruz Efectuada
  if source == 'ri_tax_retencion_iibb_formosa_efectuada':
    return 'account_base_config.account_tax_271'
  # Retención Santa Fe Efectuada
  if source == 'ri_tax_retencion_iibb_santafe_efectuada':
    return 'account_base_config.account_tax_272'
  # Retención IIBB Santiago del Estero Efectuada
  if source == 'ri_tax_retencion_iibb_santiagodelestero_efectuada':
    return 'account_base_config.account_tax_273'
  # Retención IIBB Tierra del Fuego Efectuada
  if source == 'ri_tax_retencion_iibb_tierradelfuego_efectuada':
    return 'account_base_config.account_tax_274'
  # Retención IIBB Tucuman Efectuada
  if source == 'ri_tax_retencion_iibb_tucuman_efectuada':
    return 'account_base_config.account_tax_275'
  # Percepción IIBB Chubut Efectuada
  if source == 'ri_tax_percepción_iibb_chubut_efectuada':
    return 'account_base_config.account_tax_210'
  # Percepción IIBB Tierra del Fuego Efectuada
  if source == 'ri_tax_percepción_iibb_tierradelfuego_efectuada':
    return 'account_base_config.account_tax_228'
  # Percepción IIBB Tucuman Efectuada
  if source == 'ri_tax_percepción_iibb_tucuman_efectuada':
    return 'account_base_config.account_tax_229'
  # Percepción IIBB Córdoba Efectuada
  if source == 'ri_tax_percepción_iibb_cordoba_efectuada':
    return 'account_base_config.account_tax_211'
  # Percepción IIBB ARBA Efectuada
  if source == 'ri_tax_percepción_iibb_arba_efectuada':
    return 'account_base_config.account_tax_022'
  # Percepción IIBB Misiones Efectuada
  if source == 'ri_tax_percepción_iibb_misiones_efectuada':
    return 'account_base_config.account_tax_219'
  # Percepción IIBB San Luis Efectuada
  if source == 'ri_tax_percepción_iibb_sanluis_efectuada':
    return 'account_base_config.account_tax_224'
  # Percepción IIBB Santa Cruz Efectuada
  if source == 'ri_tax_percepción_iibb_santacruz_efectuada':
    return 'account_base_config.account_tax_225'
  # Percepción IIBB Corrientes Efectuada
  if source == 'ri_tax_percepción_iibb_corrientes_efectuada':
    return 'account_base_config.account_tax_212'
  # Percepción IIBB Mendoza Efectuada
  if source == 'ri_tax_percepción_iibb_mendoza_efectuada':
    return 'account_base_config.account_tax_218'
  # Percepción IIBB La Rioja Efectuada
  if source == 'ri_tax_percepción_iibb_larioja_efectuada':
    return 'account_base_config.account_tax_210'
  # Percepción IIBB Entre Ríos Efectuada
  if source == 'ri_tax_percepción_iibb_entrerios_efectuada':
    return 'account_base_config.account_tax_213'
  # Percepción IIBB SANTA FE Efectuada
  if source == 'ri_tax_percepcion_iibb_santafe_efectuada':
    return 'account_base_config.account_tax_226'
  # Percepción IIBB LA PAMPA Efectuada
  if source == 'ri_tax_percepcion_iibb_lapampa_efectuada':
    return 'account_base_config.account_tax_216'
  # Percepción IIBB RIO NEGRO Efectuada
  if source == 'ri_tax_percepcion_iibb_rionegro_efectuada':
    return 'account_base_config.account_tax_221'
  # Percepción IIBB JUJUY Efectuada
  if source == 'ri_tax_percepcion_iibb_jujuy_efectuada':
    return 'account_base_config.account_tax_215'
  # Percepción IIBB FORMOSA Efectuada
  if source == 'ri_tax_percepcion_iibb_formosa_efectuada':
    return 'account_base_config.account_tax_214'
  # Percepción IIBB NEUQUEN Efectuada
  if source == 'ri_tax_percepcion_iibb_neuquen_efectuada':
    return 'account_base_config.account_tax_220'
  # Percepción IIBB CHACO Efectuada
  if source == 'ri_tax_percepcion_iibb_chaco_efectuada':
    return 'account_base_config.account_tax_209'
  # Percepción IIBB SANTIAGO DEL ESTERO Efectuada
  if source == 'ri_tax_percepcion_iibb_santiagodelestero_efectuada':
    return 'account_base_config.account_tax_227'
  # Percepción IIBB CATAMARCA Efectuada
  if source == 'ri_tax_percepcion_iibb_catamarca_efectuada':
    return 'account_base_config.account_tax_208'
  # Retenciones SUSS Sufrida
  if source == 'ri_tax_retencion_suss_sufrida':
    return 'l10n_ar_retentions_basic.tax_retencion_suss_sufrida'
  # Retenciones Ganancias Sufrida
  if source == 'ri_tax_retencion_ganancias_sufrida':
    return 'l10n_ar_retentions_basic.tax_retencion_ganancias_sufrida'
  # Retenciones SUSS Efectuada
  if source == 'ri_tax_retencion_suss_efectuada':
    return 'l10n_ar_retentions_basic.tax_retencion_suss_efectuada'
  # Retenciones Ganancia Efectuada
  if source == 'ri_tax_retencion_ganancias_efectuada':
    return 'l10n_ar_retentions_basic.tax_retencion_ganancias_efectuada'
  # Percepción IIBB San Juan Efectuada
  if source == 'ri_tax_percepcion_iibb_sanjuan_efectuada':
    return 'account_base_config.account_tax_223'
  # Percepción IIBB Salta Efectuada
  if source == 'ri_tax_percepcion_iibb_salta_efectuada':
     return 'account_base_config.account_tax_222'
  # Retención IIBB Formosa Sufrida
  if source == 'ri_tax_retencion_iibb_formosa_sufrida':
     return 'account_base_config.account_tax_283'

  # ninguno de los anteriores devuelvo excepcion
  raise Exception('Identificador externo no encontrado en migration script. %s' % source)
  #return 'account_base_config.account_tax_005'

# obtener el identificador externo en source
model = source_connection.model('account.invoice.line')
source_external_id = model.export_data([rec_id], ['invoice_line_tax_id/id'])['datas'][0][0]

# mapear identificador externo de source a target y devolverlo
context['result'] = map_tax(source_external_id) if source_external_id else False
