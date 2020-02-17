[![Build Status](https://travis-ci.org/jobiols/odoo-etl.svg?branch=12.0)](https://travis-ci.org/jobiols/odoo-etl)
[![CodeFactor](https://www.codefactor.io/repository/github/jobiols/odoo-etl/badge)](https://www.codefactor.io/repository/github/jobiols/odoo-etl)

odoo-etl Ported from v9 to v12 by jeo Software

Odoo data manipulation, like an small ETL (Extract, Transform and Load) for odoo databases.

The main idea of the project is to give functional users the availability to move data from one odoo database to another odoo database. The design is quite simple, it use native odoo methods (primarily load and export_data).

The aim of this project is different from odoo migration or OpenUpgrade, it allows to start from a clean database, merging  different odoo databases into a single multicompany db, etc.

This project was developed by a non developer so for sure you are gonna find lot of ugly statements and ideas.

It was developed using xmi2oerp tool, thanks Cristian Sebastian Rocha for that great work!

You can see an ugly example video in the following links, in this example we are going to show how to move data from a v6.1 database with demo data to a trunk database without demo data. Links:
* https://www.youtube.com/watch?v=HZQQaNQ9k7U
* https://www.youtube.com/watch?v=VmScwCM3whg
* https://www.youtube.com/watch?v=PS2ShlY1gLI

Any feedback is welcome, if someone likes the idea, please don't hesitate to contact us so we can work together.

You can find some kind of tutorial on: https://docs.google.com/document/d/1HWERCUp9rMHqEibT7B_mfu9jePV-FBkYbo--OB0jXqA



## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
