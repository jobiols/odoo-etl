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
    'author': 'INFINITY SOLUTIONS, ADHOC SA, jeo Software',
    'category': 'Tools',
    'version': '13.0.0.0.0',
    'license': 'AGPL-3',
    'name': 'odoo ETL',
    "development_status": "Alpha",  # "Alpha|Beta|Production/Stable|Mature"
    'test': [],
    'website': 'http://jeosoft.com.ar',
    'depends': ['base', 'account'],
    'data': [
        'security/etl_group.xml',
        'views/etl_menuitem.xml',
        'views/value_mapping_field_view.xml',
        'views/external_model_view.xml',
        'views/external_model_record_view.xml',
        'views/field_mapping_view.xml',
        'views/field_view.xml',
        'views/action_view.xml',
        'views/manager_view.xml',
        'views/value_mapping_field_value_view.xml',
        'views/value_mapping_field_detail_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'external_dependencies': {
        'python': [
            'erppeek',
        ],
    },
}
