After installing ETL module, navigate to ETL’s manager model and create a new manager
with the following details:
**Name** field contains the name of your manager without any specific restriction for the name.

**Target ID Type** field is a selection field with possible values *Source ID* or *Builded ID*.
    When set to *Source ID*, the record XML ID that will be used in the migration process
    will be according to the default source exported external ID. On the other hand,
    when set to *Builded ID*, the record XML ID that will be used in the migration process
    will be customized according to the prefix set later at an additional field. The usage
    of *source ID* is recommended when performing migration process.

**Source Hostname** field should be the source database host URL that is used to access
    the Odoo database from remote OS. For example: http://192.168.1.101.

**Source Port** field should be the source database port that is used to access the Odoo
    database. For example: 8069.

**Source Database** field should be the source database name.

**Source Login** field should be the username that is used to login to the source
    database from the login page. Make sure the user have a full access to all the models.

**Source Password** field should be the password according to the username that is
    used to login to the source database from the login page.

**Source Language** field is the source database default language. It’s recommended to
    keep the language as default (en_US).

**Target Hostname** field should be the target database host URL that is used to access
    the Odoo database from remote OS. For example: http://192.168.1.101.

**Target Port** field should be the target database port that is used to access the Odoo
    database. For example: 8069.

**Target Database** field should be the target database name.

**Target Login** field should be the username that is used to login to the target
    database from the login page. Make sure the user have a full access to all the models.

**Target Password** field should be the password according to the username that is
    used to login to the target database from the login page.

**Target Language** field is the target database default language. It’s recommended to
    keep the language as default (en_US)

Preparing the Target Database for Migration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Make sure the target database is created and all the modules that will receive the records
from the source	database are installed. For example if you’re performing the migration for HR
and	Projects, make sure	the	HR and Projects modules are installed in the target/destination
database and of course the source database.

Read Databases
~~~~~~~~~~~~~~

To read the models and get the record counts from the source and the target/destination 
database click **Read and Get Record** from the action bar. The ETL module will now attempt
to connect and read from the source and destination databases.

After the process is done, the **External Models** tab from your manager form view should
contain the list of models that have been read from the source and target database (along 
with its fields when clicked) and record counts.

Mapping
~~~~~~~

Matching the source models and the target models along with its fields can be done 
automatically by ETL; however, the result may not be perfectly correct. Some models and 
fields that changes across the version may have to be manually matched which will be 
explained in the next section. To perform an automatic model and fields mapping, simply 
click **Match and Order** from the action bar.

After the process is done, the Actions tab from your manager form view should contain the 
list of actions (model mappings) that have been matched and ordered by ETL.

Test Actions
~~~~~~~~~~~~

At the first use of the ETL manager, it’s necessary to test the actions one by one which also 
means the migration will happen model by model for the first time. An action represents a 
migration for a single model at a time. Actions can also be understood as model mapping. 
It’s not necessary to configure all the actions/model mapping implied by the Match and 
Order action, but only the required actions/model mapping necessary for the intended 
migration. 
 
To be able to configure the actions and test it, simply click it from the list of actions in the 
manager.

Following is the details about the fields in the action model:

**Name** field should be the name of the action which is usually automated from the
Match and Order previous action.

**Source Domain** field is used to apply domain for the source database model when
performing the migration to filter out or include certain records in the migration.

**Blocked** field is used to block the actions from running instead of having to switch
the status to disabled. This field is used when configuring and testing the action on 
the first run of migration. After done configuring the action, Blocked field will usually 
be checked then later unchecked when performing the real migration which will be 
explained in the next section.

• Sequence field is used to order the action. The order for which action (model) will be 
performed first is really important due to the dependencies between models. For 
example, the sequence of customer tags model should be lower than the customer 
model since migration of the customer model will require the existing records of tags 
when the field of tag_ids is enabled (field configuration will be explained in the next 
section).

• Repeating Action field is a read-only field which will be automatically checked when 
the one of the fields state in the action’s Field Mapping list is set to on_repeating. 
When this field is checked, the Run Repeated Action button will appear in the action 
bar of the Actions model form.

• From Record field is also used to filter out or include records in the migration 
process. The records that will be migrated will start from the value set at this field. 
To disable this feature, simply leave it along with the To Record field to its default 
value 0 (zero).

• To Record field is also used to filter out or include records in the migration process. 
The records that will be migrated will end at the value set at this field. To disable this 
feature, simply leave it along with the From Record field to its default value 0 (zero). 
Copyright © PT. Vikasa Infinity Anugrah. All rights reserved. 

Source Model field contains selections of the source model name. 
source_id_exp field is the field name of the ID field in the source model. Usually is set 
at its default (id). 
Source Records is a read only field counting the number of records at the source 
database in relation to the selected source model. Number of non-active records will 
not be counted, but can still be included in migration by setting the domain [‘|’, 
(‘active’, ‘=’, True), (‘active’, ‘=’, False)] 
Target Model field contains selections of the target model name which will be 
mapped to receive the records from the source model when running the action. 
Target ID Type field have the same function as the Target ID Type field of the 
manager model. The default value will follow the value set at the Target ID Type field 
of the manager model and can be changed in every action according to preference 
(not recommended). 
Target Records is a read only field counting the number of records at the 
destination/target database in relation to the selected target model. Number of non-
active records will not be counted. 
target_id_prefix field will only appear when the Target ID Type field is set to Builded 
ID allowing the customization of the records XML id instead of using the default 
export external ID. 
 
The Action fields are usually set correctly by the automatic Match and Order action. Beside 
configuring the fields, it’s very important to set the action’s state which can be changed to 
the following possible state:

• Enabled state should be set to an action that will be included in the migration 
process.

• To Analyse state should be set to an action that require a further analysis and 
testing. When an action is set to this state, it will not be included when running the 
migration process.

• Disabled state should be set to an action that will not be included in the migration 
process.

• No Records state should be set to an action that will not be included in the migration 
process due to 0 records found in the source model. 
 
After correctly configuring and checking the Action fields, it’s very important to also check 
and configure every line of field mapping in the field mapping list in every actions. The field 
mapping determines which field of the selected model to be included or excluded in the 
migration process. To configure the fields, simply click the field mapping from the field 
mapping list of the action form.
