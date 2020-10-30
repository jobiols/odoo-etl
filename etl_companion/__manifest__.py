#
##############################################################################
#
#    Copyright (C) 2020  jeo Software  (http://jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'author': 'jeo Software',
    'category': 'Tools',
    'version': '13.0.0.0.3',
    'license': 'AGPL-3',
    'name': 'odoo ETL companion',
    "development_status": "Alpha",  # "Alpha|Beta|Production/Stable|Mature"
    'test': [],
    'website': 'http://jeosoft.com.ar',
    'depends': ['base', 'account', 'l10n_latam_invoice_document', 'l10n_latam_base', 'l10n_ar'],
    'data': [
        'data/account_group_data.xml',
        'data/account_chart_template_data.xml',
        'data/account.account.template.csv',
        'data/account_chart_template_data2.xml',
    ],
    'installable': True,
    'application': False,
}
