## Where to install ETL

As we could seen in the introduction, the ETL etl module can be installed in 
an odoo external to the source and the target.

However, if the connection between the systems is made over the internet and 
the amount of data to be moved is large. It would be convenient to install 
ETL in odoo target.

On the other hand, the advantage of having Odoo on an independent basis is 
that the know-how of migration remains in the database.

The ideal situation is when source, target and ETL are in different odoo 
installations and all of them are in the same lan.
