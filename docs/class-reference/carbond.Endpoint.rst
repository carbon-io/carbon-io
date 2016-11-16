================
carbond.Endpoint
================

.. js:class:: Endpoint()
    :hidden:

An ``Endpoint`` is a representation of a RESTFul resource. Each endpoint can implement one or more operations representing each of the HTTP methods: ``GET``, ``PUT``, ``POST``, ``CREATE``, ``DELETE``, ``HEAD``, ``OPTIONS``.

Endpoints can also define child endpoints whose paths will be interpreted relative to the ``path`` of this ``Endpoint`` object.

Configuration
=============

..  code-block:: javascript

    {
      _type: carbon.carbond.Endpoint,

      [parameters: {
        <name> : <OperationParameter>
      }]  

      [get: <function> | <Operation>],
      [put: <function> | <Operation>],
      [post: <function> | <Operation>],
      [create: <function> | <Operation>],
      [delete: <function> | <Operation>],
      [head: <function> | <Operation>],
      [options: <function> | <Operation>],

      [endpoints: { 
        <path>: <Endpoint>
        ...
      }]
    }

Properties
==========

- ``path (read-only)``: The path to which this endpoint is bound. The path can contain variable patterns (e.g. ``'orders/:id'``). The ``path`` property is not configured directly on ``Endpoint`` objects but are specified as lvals in enclosing definitions of endpoints such as in an ``ObjectServer`` or a parent ``Endpoint`` object. When retrieved the value of this property will be the absolute path of the endpoint from ``/``.

- ``parent (read-only)``: The parent ``Endpoint`` of this ``Endpoint``.

- ``objectserver (read-only)``: The :js:class:`ObjectServer` to which this endpoint belongs.

- ``parameters``: A mapping of parameter names to ``OperationParameter`` objects. Parameters defined for an ``Endpoint`` are inherited by all operations of this ``Endpoint`` as well as by all child ``Endpoints`` of this ``Endpoint``.

- ``endpoints``: A set of child ``Endpoint`` definitions. This is an object whose keys are path strings and values are instances of ``Endpoint``. Each path key will be interpreted as relative to this Endpoints ``path`` property.

Operations
==========

Each endpoint can implement one or more operations representing each of the HTTP methods: ``GET``, ``PUT``, ``POST``, ``CREATE``, ``DELETE``, ``HEAD``, ``OPTIONS``. There is no requirement an endpoint implement all HTTP methods. It only needs to implement those it wishes to support.

Each operation is represented as either:

- A function of the form ``function(req, res)``
- An ``Operation`` object. This is more elaborate definition which allows for a description, parameter definitions, and other useful meta-data as well as a ``service`` method of the form ``function(req, res)``
  
When responding to HTTP requests, two styles are supported:

- An asynchronous style where operations write directly to the ``HttpResponse`` object passed to the operation. This style is useful when the operation needs to manipulate the ``HttpResponse`` object to do more than simply return JSON (e.g. set HTTP headers), or wished to pass the response to other functions.
- A synchronous style where the operation simply returns a JSON object from the operation, or throws an exception to signal an error condition. When using this style the ``HttpResponse`` parameter can be omitted from the function signature of the operation. This style is useful when programming in a more synchronous style and / or coordinating with exceptions thrown deeper in the call stack.

Examples (synchronous)
----------------------

..  code-block:: javascript

    get: function(req) {
      return { msg: "hello world!" }
    }

..  code-block:: javascript

    get: {
      description: "My hello world operation",
      params: {}
      service: function(req) {
        return { msg: "hello world!" }
      }
    }

XXX come back to talk about error handling

Operation details
=================

get
---

Implementation of HTTP ``GET``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

put
---

Implementation of HTTP ``PUT``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

post
----

Implementation of HTTP ``POST``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

create
------

Implementation of HTTP ``CREATE``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

delete
------

Implementation of HTTP ``DELETE``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

head
----

Implementation of HTTP ``HEAD``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

options
-------

Implementation of HTTP ``OPTIONS``. Either a ``function`` or an ``Operation`` object.

If the operation is defined by a function it will have these parameters:

- ``req``: the ``HttpRequest`` object
- ``res``: the ``HttpResponse`` object (can be omitted if using a synchronous style). If the operation is defined by an ``Operation`` object the definition will have a service method of the same signature.

Examples
========

..  code-block:: javascript

    var carbon = require('carbon.io')
    var o = carbon.atom.o(module)

    module.exports = o({
      _type: carbon.carbond.ObjectServer,
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