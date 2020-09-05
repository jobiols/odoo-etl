#:banner: banners/web_service_api.jpg
#:types: api

:code-column:

============
Introduction
============


Odoo is usually extended internally via modules, but many of its features and
all of its data are also available from the outside for external analysis or
integration with various tools. Part of the :ref:`reference/orm/model` API is
easily available over XML-RPC_ and accessible from a variety of languages.

.. Odoo XML-RPC idiosyncracies:
   * uses multiple endpoint and a nested call syntax instead of a
     "hierarchical" server structure (e.g. ``odoo.res.partner.read()``)
   * uses its own own manual auth system instead of basic auth or sessions
     (basic is directly supported the Python and Ruby stdlibs as well as
     ws-xmlrpc, not sure about ripcord)
   * own auth is inconvenient as (uid, password) have to be explicitly passed
     into every call. Session would allow db to be stored as well
   These issues are especially visible in Java, somewhat less so in PHP
