# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Argentinian Accounting Migration',
    'version': "13.0.1.0",
    'description': """

    Este modulo deberia agregar las modificaciones necesarias para la migracion


""",
    'author': 'Quilsoft SA',
    'category': 'Localization',
    'depends': [
        'l10n_ar',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/l10n_latam_identification_type_data.xml',
        'data/l10n_ar_afip_responsibility_type_data.xml',
        'data/account_group_data.xml',
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_data2.xml',
        'data/account_tax_group.xml',
        'data/account_tax_template_data.xml',
        'data/account_fiscal_template.xml',
        'data/uom_uom_data.xml',
        'data/l10n_latam.document.type.csv',
        'data/res_partner_data.xml',
        'data/res.currency.csv',
        'data/res.country.csv',
        'views/account_move_view.xml',
        'views/res_partner_view.xml',
        'views/res_company_view.xml',
        'views/res_country_view.xml',
        'views/afip_menuitem.xml',
        'views/l10n_ar_afip_responsibility_type_view.xml',
        'views/res_currency_view.xml',
        'views/account_fiscal_position_view.xml',
        'views/uom_uom_view.xml',
        'views/account_journal_view.xml',
        'views/l10n_latam_document_type_view.xml',
        'views/ir_sequence_view.xml',
        'views/report_invoice.xml',
        'report/invoice_report_view.xml',
    ],
    'demo': [
        # we create demo data on different companies (not main_company) to
        # allow different setups and also to allow multi-localization demo data
        'demo/exento_demo.xml',
        'demo/mono_demo.xml',
        'demo/respinsc_demo.xml',
        'demo/res_partner_demo.xml',
        'demo/account_tax_demo.xml',
        'demo/product_product_demo.xml',
        'demo/account_customer_invoice_demo.xml',
        'demo/account_customer_refund_demo.xml',
        'demo/account_supplier_invoice_demo.xml',
        'demo/account_supplier_refund_demo.xml',
        # restore
        'demo/res_users_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
