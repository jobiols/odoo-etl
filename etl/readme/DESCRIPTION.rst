Odoo data manipulation, like an small ETL (Extract, Transform and Load)
for odoo databases.

The main idea of the project is to give functional users the availability to
move data from one odoo database to another odoo database.
The design is quite simple, it use native odoo methods (primarily load and export_data).

The aim of this project is different from odoo migration or OpenUpgrade,
it allows to start from a clean database, merging  different odoo databases
into a single multicompany db, etc.

It was developed using xmi2oerp tool, thanks Cristian Sebastian Rocha for
that great work!

Este proceso corre en un odoo separado del cliente y del target, se conecta
con el clietne para leer los datos y con el target para poner los datos.
En su base se almacena la informacion de como es la migracion.
