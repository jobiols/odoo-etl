# Introduction to ETL

ETL is an Odoo module developed to move data between databases easily. 
It can be used for data migration between same or different odoo versions 
(v8 to v13). 
ETL Stands for Extract Transform and Load, and can be running in an 
intermediate database see *picture 1*. In this schema, database A can be the 
source Odoo database version X and database B can be target Odoo database version Y.

See the section *Where to install ETL* to understand performance issues.

![](/assets/img/etl-dbs.png)
*<center>Picture 1</center>*

The aim of this project is different from odoo migration or OpenUpgrade, it 
allows to start from a clean database, merging  different odoo databases into 
a single multicompany db.

The proyect lives in [odoo-etl](https://github.com/jobiols/odoo-etl) Any feedback 
is welcome, if someone likes the idea, please don't hesitate to contact me so 
we can work together. 

If you find some issues please report it to [issues](https://github.com/jobiols/odoo-etl/issues)

Jorge Obiols <jorge.obiols@gmail.com>

{% include capitulo2.md %}
{% include capitulo3.md %}
{% include where-to-install.md %}
