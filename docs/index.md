# Introduction to ETL

ETL is an Odoo module developed to move data between databases easily. 
It can be used for data migration between same or different odoo versions 
(v8 to v13).

ETL Stands for Extract Transform and Load, and can be running in an intermediate
database see picture 1.

![image](/_includes/potenciar.jpeg)

The main idea of the module is to give functional users the availability to 
move data from one odoo database to another odoo database. The design is quite 
simple, it use native odoo methods (primarily load and export data).

The aim of this project is different from odoo migration or OpenUpgrade, it 
allows to start from a clean database, merging  different odoo databases into 
a single multicompany db, etc.

The proyect lives in github.com/jobiols/odoo-etl Any feedback is welcome, 
if someone likes the idea, please don't hesitate to contact me so we can work 
together. 

Jorge Obiols <jorge.obiols@gmail.com>

sigue la linea

{% include capitulo1.md %}
{% include capitulo2.md %}
{% include capitulo3.md %}
{% include capitulo4.md %}



