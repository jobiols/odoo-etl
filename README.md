[![Build Status](https://travis-ci.com/jobiols/odoo-etl.svg?branch=12.0)](https://travis-ci.com/jobiols/odoo-etl)
[![codecov](https://codecov.io/gh/jobiols/odoo-etl/branch/12.0/graph/badge.svg)](https://codecov.io/gh/jobiols/odoo-etl)
[![Maintainability](https://api.codeclimate.com/v1/badges/0b6ff580f00ba4b0fb21/maintainability)](https://codeclimate.com/github/jobiols/odoo-etl/maintainability)
[![CodeFactor](https://www.codefactor.io/repository/github/jobiols/odoo-etl/badge)](https://www.codefactor.io/repository/github/jobiols/odoo-etl)

odoo-ETL Ported from v9 to v12 by jeo Software.
===============================================

## This is an alpha version not fully tested.

Odoo data manipulation, like an small ETL (Extract, Transform and Load) for odoo databases.

The main idea of the project is to give functional users the availability to move data from one odoo database to another odoo database. The design is quite simple, it use native odoo methods (primarily load and export_data).

The aim of this project is different from odoo migration or OpenUpgrade, it allows to start from a clean database, merging  different odoo databases into a single multicompany db, etc.

You can see several example video made by jjscarafia (in spahish) The videos are from the old odoo v9 but it looks almost the same.
Links:

* [video 1](https://www.youtube.com/watch?v=HZQQaNQ9k7U)
* [video 2](https://www.youtube.com/watch?v=VmScwCM3whg)
* [video 3](https://www.youtube.com/watch?v=PS2ShlY1gLI)

Please see [github pages](https://jobiols.github.io/odoo-etl/) for the latest information.

Any feedback is welcome, if someone likes the idea, please don't hesitate to contact me so we can work together.

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
