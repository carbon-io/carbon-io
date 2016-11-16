==============
Access Control
==============

.. toctree::

``Services``\s accomplish access control by way of ACLs or *Access Control Lists*. 

ACLs
----

Carbond provides a very generic and extensible ACL framework. In their
most generic form, ``Acl`` objects map *Users* and *Groups* to a set
of *Permissions* which govern access to some entity.

In practice you will use one of the pre-packaged ACL types to gate
access to your ``Endpoints`` and their ``Operations``.

Endpoint ACLs 
------------- 

All ``Endpoints`` can be configured with an ``EndpointAcl`` to govern
which endpoint ``Operations`` can be accessed by users.

``EndpointAcl``\s defined the following permissions, one for each HTTP method:

* ``get``
* ``post``
* ``put``
* ``patch``
* ``delete``
* ``head``
* ``options``

All permissions default to ``false`` except the ``options`` permission
which defaults to ``true``.

Here is an example of a ``Service`` using an ``EndpointAcl``:

..  code-block:: javascript 
  :linenos:
  :emphasize-lines: 13-49

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module).main 
  var __ = carbon.fibers.__(module).main

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      endpoints: {
        hello: o({
          _type: carbon.carbond.Endpoint,

          acl: o({
            _type: carbon.carbond.security.EndpointAcl

            groupDefinitions: { // This ACL defined two groups, 'role' and 'title'.
              role: 'role' // We define a group called 'role' based on the user property named 'role'.
              title: function(user) { return user.title } 
            }
            entries: [
              {
                user: { role: "Admin" },
                permissions: {
                  "*": true // "*" grants all permissions 
                }
              },
              {
                user: { title: "CFO" },
                permissions: { // We could have used "*" here but are being explicit. 
                  get: true,
                  post: true
                }
              },
              {
                user: "12345", // User with _id "12345"
                permissions: { 
                  get: false,
                  post: true
                }
              },
              {
                user: "*" // All other users
                permissions: { 
                  get: true,
                  post: false,
                }
              }
            ]
          }),

          get: function(req) {
            return { msg: "Hello World!" }
          },

          post: function(req) {
            return { msg: "Hello World! " + req.body }
          }

        })
      })
    }) 
  })


Collection ACLs 
---------------

``CollectionAcl``\s are similar to ``EndpointAcl``\s except that they
define a set of permissions that matches the ``Collection`` interface.

``CollectionAcl``\s define the following permissions:

* ``insert``
* ``find``
* ``update``
* ``remove``
* ``saveObject``
* ``findObject``
* ``updateObject``
* ``removebject``

All permissions default to ``false``.

Here is an example of a ``Service`` using a ``CollectionAcl`` on a ``MongoDBCollection``:

..  code-block:: javascript 
  :linenos:
  :emphasize-lines: 14-50

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module).main 
  var __ = carbon.fibers.__(module).main

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      endpoints: {
        hello: o({
          _type: carbon.carbond.mongodb.MongoDBCollection,
          collection: 'zipcodes',

          acl: o({
            _type: carbon.carbond.security.CollectionAcl

            groupDefinitions: { // This ACL defined two groups, 'role' and 'title'.
              role: 'role' // We define a group called 'role' based on the user property named 'role'.
              title: function(user) { return user.title } 
            }
            entries: [
              {
                user: { role: "Admin" },
                permissions: {
                  "*": true // "*" grants all permissions 
                }
              },
              {
                user: { title: "CFO" },
                permissions: { 
                  find: true,
                  findObject: true,
                  "*": false // This is implied since the default value for all permissions is ``false``.
                }
              },
              {
                user: "12345", // User with _id "12345"
                permissions: { 
                  insert: true,
                  findObject: true
                }
              },
              {
                user: "*" // All other users
                permissions: { 
                  findObject: true
                }
              }
            ]
          })

        }) 
      }
    }) 
  })


Re-using ACLs across multiple Endpoints
---------------------------------------

In some cases you may wish to re-use the same ACL across many
``Endpoints``\s. To do this you can simply define your ACL as its own
component and then reference it in your ``Endpoint``.

**Example**

MyAcl.js:

..  code-block:: javascript 
  :linenos:

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module).main 
  var __ = carbon.fibers.__(module).main

  module.exports = o({
    _type: carbon.carbond.security.CollectionAcl,
    .
    . // Your ACL definition
    .
  })

Now you can reference this ACL from any ``Endpoint`` that wished to
use that ACL:


..  code-block:: javascript 
  :linenos:
  :emphasize-lines: 4, 14

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module).main 
  var __ = carbon.fibers.__(module).main
  var _o = carbon.bond._o(module)

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      endpoints: {
        hello: o({
          _type: carbon.carbond.mongodb.MongoDBCollection,
          collection: 'zipcodes',
          acl: _o('./MyAcl')
        }) 
      }
    }) 
  })
