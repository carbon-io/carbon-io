===========================
Services
===========================

.. toctree::

APIs are defined via ``Service``\ s. Put simply, an ``Service`` is an 
HTTP server that exposes a JSON REST API and which is defined as a 
tree of ``Endpoint``\s. 

Services and Endpoints
----------------------

All ``Service`` definitions follow the same general structure:

..  code-block:: javascript 

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module) 
  var __ = carbon.fibers.__(module, true) 

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      endpoints: {
        // Endpoint definitions go here
      }
    })
  })

Here is an example of a simple ``Service`` that runs on port ``8888``
and that defines a single ``Endpoint`` at the path ``/hello`` which a
defines a single ``get`` operation:

..  code-block:: javascript 

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
          }
        }) 
      }
    }) 
  })

Service middleware 
------------------

You can register Express-style middleware for your service via the ``middleware``
property on your ``Service`` object:

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 9-14

  var carbon = require('carbon-io')
  var o  = carbon.atom.o(module).main
  var __ = carbon.fibers.__(module).main

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      middleware: [
        function(req, res, next) {
          console.log("This is called on every request")
          next()
        } 
      ]
      endpoints: {
        // Endpoint definitions go here
      }
    }) 
  }) 

Running Services from the command line
--------------------------------------

In most cases you will want to start and stop your ``Service`` from
the command line.

This can be done by ensuring the value of ``o`` you are using to
define your ``Service`` is the ``main`` version of the library, as
shown below on line 2:

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 2

  var carbon = require('carbon-io')
  var o  = carbon.atom.o(module).main
  var __ = carbon.fibers.__(module).main

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888
    }) 
  }) 

You can then start your ``Service`` like this:

..  literalinclude:: /frags/shell-output-starting-service.rst 
    :language: sh 

You can use ``-h`` or ``--help`` to get command help from your
``Service``:

..  literalinclude:: /frags/shell-output-service-help.rst 
    :language: sh 

You can see that there are two sub-commands. One for starting the
server and another for generating documentation for your ``Service``.

The default sub-command is ``start-server``: 

..  literalinclude:: /frags/shell-output-service-ss-help.rst 
    :language: sh 

Running Services from code
--------------------------

While you will usually run your ``Service``\s via the commandline as a
top-level application, ``Service`` objects can also be used as a
library. 

By using the ``start`` and ``stop`` methods, you can manage the
``Service`` lyfecyle manually. 

These methods have both an asynchronous and a synchronous interface:

**Asynchronous example**

..  code-block:: javascript 

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module) 
  var __ = carbon.fibers.__(module) 

  var myService = o({
    _type: carbon.carbond.Service,
    port: 8888 
    . 
    . 
    . 
  }) 

  myService.start({}, function(err) {
    if (err) {
      myService.logError("Error starting service " + err) 
    } else {
      myService.logInfo("Service started" + err) 
      //
      // Do stuff...
      //
      myService.stop(function(err) {
        myService.logInfo("Service stopped") 
      }) 
    }
  })

**Synchronous example**

..  code-block:: javascript 

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module) 
  var __ = carbon.fibers.__(module) 

  var myService = o({
    _type: carbon.carbond.Service,
    port: 8888 
    . 
    . 
    . 
  }) 

  // Run in a fiber
  __(function() { 
    try {
      myService.start()
      //
      // Do stuff...
      //
      myService.stop()
    } catch (e) {
      myService.logError(e)
    }
  })
