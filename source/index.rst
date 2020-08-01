Documentation for odoo-etl module for Odoo V12
==============================================

It is a data manipulation, like an small ETL (Extract, Transform and Load) for
odoo databases.

The main idea of the project is to give functional users the availability to 
move data from one odoo database to another odoo database. The design is quite 
simple, it use native odoo methods (primarily load and export_data).

The aim of this project is different from odoo migration or OpenUpgrade, it 
allows to start from a clean database, merging  different odoo databases into 
a single multicompany db, etc.

The proyect lives in `github.com/jobiols/odoo-etl`_ Any feedback is welcome, 
if someone likes the idea, please don't hesitate to contact me so we can work 
together.


.. toctree::
   :maxdepth: 1
   :caption: Introduction:

   reposettings
   examples/workflow
   examples/sphinxproject
   examples/sparatebranch
   aboutmakefile

.. _github.com/jobiols/odoo-etl: https://github.com/jobiols/odoo-etl
