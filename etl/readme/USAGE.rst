* It is recommendend to delete all external identifiers on source database for
model "res_partner" because when creating a user, odoo simulates partner
creation and raise a unique constraint (except the admin user)

* Also could be recommendend to delete external identifiers related to product
and product_temlate (except service products)

* Advisable to configure xmlrpc users to timezone zero to avoid errors

* Asegurarse de tener permisos manger para este modulo.

* Es aconsejable quitar las restricciones de timeout poniendo workers=0

1- Crear un registro Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

En este formulario se ponen los datos de Fuente y Destino de las instancias
de odoo para las que vamos a trabajar.

1- Leer los modelos
~~~~~~~~~~~~~~~~~~~

Con el boton **READ MODELS** se leen los modelos de las instancias Fuente y Destino
y luego de la carga se pueden ver en la pestaña **External Models**

el boton **GET RECORD NUMBER** lee la cantidad de registros en cada modelo

