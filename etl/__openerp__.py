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
    'author': u'INFINITY SOLUTIONS, ADHOC SA, jeo Software',
    'category': u'Tools',
    'version': u'13.0.0.0.0',
    'license': 'AGPL-3',
    'name': u'odoo ETL',
    "development_status": "Alpha",  # "Alpha|Beta|Production/Stable|Mature"
    'test': [],
    'website': 'http://jeosoft.com.ar',
    'depends': ['base'],
    'data': [
        u'security/etl_group.xml',
        u'views/etl_menuitem.xml',
        u'views/value_mapping_field_view.xml',
        u'views/external_model_view.xml',
        u'views/external_model_record_view.xml',
        u'views/field_mapping_view.xml',
        u'views/field_view.xml',
        u'views/action_view.xml',
        u'views/manager_view.xml',
        u'views/value_mapping_field_value_view.xml',
        u'views/value_mapping_field_detail_view.xml',
        u'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'external_dependencies': {
        'python': [
            'erppeek',
        ],
    },

}
