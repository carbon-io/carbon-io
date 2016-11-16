===========================
Endpoints
===========================

.. toctree::

Each ``Endpoint`` represents a single URI and can support any number
of the HTTP operations: ``GET``, ``POST``, ``PUT``, ``PATCH``,
``DELETE``, ``HEAD``, and ``OPTIONS``.

Simple Endpoints
----------------

Below is a simple ``Endpoint`` at the path ``/hello`` that defines two
operations, ``get`` and ``post``:

..  code-block:: javascript 
  :linenos:
  :emphasize-lines: 10-18

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
          get: function(req) {
            return { msg: "Hello World!" }
          },
          post: function(req) {
            return { msg: "Hello World! " + req.body }
          }
        }) 
      }
    }) 
  })

Endpoints with templated paths 
------------------------------

``Endpoint``\ s can be defined using templated paths. Bound template
variables values can then be accessed via ``req.params``:

..  literalinclude:: /examples/objectserver-endpoint.js 
    :language: javascript 
    :linenos:
    :emphasize-lines: 17, 21

In this example, a request for the path ``/users/jonny16`` will route to
the ``/users/:id`` ``Endpoint`` and ``req.params.user`` will have the value ``"jonny16"``. 


Sub-endpoints 
-------------

``Endpoints``\s may contain sub-endpoints. Here is an example that is
similar to the API as above, but that uses a sub-endpoint to define an
``Endpoint`` at the path ``/users/:id``.

..  code-block:: javascript
    :linenos:
    :emphasize-lines: 16, 20

    var carbon = require('carbon-io')
    var o  = carbon.atom.o(module).main
    var __ = carbon.fibers.__(module).main

    __(function() {
      module.exports = o({
        _type: carbon.carbond.Service,
        port: 8888,
        endpoints: {
          'users': o({
            _type: carbon.carbond.Endpoint,
            get: function(req) {
              // get all users
            },
            endpoints: {
              ":id": o({
                _type: carbon.carbond.Endpoint,
                get: function(req) {
                  // get the user
                  return getUserById(req.params.id)
                },
                delete: function(req) {
                  // delete the user
                }
              }),
            }
          }),
        }
      })
    })

Accessing Service properties from within Endpoints 
--------------------------------------------------

Properties of the top-level ``Service`` can be accessed via the
``service`` property of your ``Endpoint``:

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 15

  var carbon = require('carbon-io')
  var o  = carbon.atom.o(module).main
  var __ = carbon.fibers.__(module).main

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      endpoints: {
        status: o({
          _type: carbon.carbond.Endpoint,
          get: function(req) {
            return { 
              running: true,
              msg: "Up and running on port: " + this.service.port 
            }
          }
        }) 
      }
    }) 
  }) 

