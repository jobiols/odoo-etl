Make sure the ERPpeek library is available in the server.
sudo pip install erppeek

You can install odoo-etl on the target system, however you can install on an 
intermediate system with some benefits. That intermediate odoo would connect 
with the source and the target. That way the migration information will be 
saved in the intermediate system and can be used to move data from other 
systems. If the installation is done on the destination system once the 
migration is complete, the most natural thing would be to eliminate the 
odoo-etl module, which would erase all the know-how of the migration.

Is advisable to set workers=0 and limit_time_real = 1200 in the odoo.conf file 
to get rid of timeout problems and please, keep an eye open to the logs.
