==========
Operations
==========

Each endpoint can implement one or more operations representing each
of the HTTP methods: ``GET``, ``PUT``, ``POST``, ``PATCH``,
``DELETE``, ``HEAD``, ``OPTIONS``. There is no requirement an endpoint
implement all HTTP methods. It only needs to implement those it wishes
to support.

Defining Operations
-------------------

Each operation is represented as either:

- A function of the form ``function(req, res)``.
- An ``Operation`` object. This is more elaborate definition which
  allows for a description, parameter definitions, and other useful
  meta-data as well as a ``service`` method of the form
  ``function(req, res)``.

When responding to HTTP requests, two styles are supported:

- An asynchronous style where operations write directly to the
  ``HttpResponse`` object passed to the operation. This style is
  useful when the operation needs to manipulate the ``HttpResponse``
  object to do more than simply return JSON (e.g. set HTTP headers),
  or wished to pass the response to other functions.
- A synchronous style where the operation simply returns a JSON object
  from the operation, or throws an exception to signal an error
  condition. When using this style the ``HttpResponse`` parameter can
  be omitted from the function signature of the operation. This style
  is useful when programming in a more synchronous style and / or
  coordinating with exceptions thrown deeper in the call stack.

**Examples (asynchronous)**

..  code-block:: javascript

    get: function(req, res) {
      res.send({ msg: "Hello World!" })  
    }

..  code-block:: javascript

    get: {
      description: "My hello world operation",
      parameters: {}
      service: function(req, res) {
        res.send({ msg: "Hello World!" })  
      }
    }

**Examples (synchronous)**

..  code-block:: javascript

    get: function(req) {
      return { msg: "Hello World!" }
    }

..  code-block:: javascript

    get: {
      description: "My hello world operation",
      parameters: {}
      service: function(req) {
        return { msg: "Hello World!" }
      }
    }

Operation parameters
--------------------

Each :rst:role:`Operation` can define the set of parameters it
takes. Each ``OperationParameter`` can specify the location of the
parameter (``'path'``, ``'query'`` (for query string), or ``'body'``) as well as a JSON schema
definition to which the parameter must conform.

All parameters provided to an ``Operation`` will be available via the
``parameters`` property of the ``HttpRequest`` object and can be
accessed as ``req.parameters[<parameter-name>]`` or
``req.parameters.<parameter-name>``.

Carbond supports both JSON and `EJSON
<http://docs.mongodb.org/manual/reference/mongodb-extended-json/>`_
(Extended JSON, which includes support additional types such as
``Date`` and ``ObjectId``).

Formally defining parameters for operations helps you to build a
self-describing API for which the framework can then auto-generate API
documention and interactive administration tools.

**Examples**

..  code-block:: javascript

    {
      get: {
        description: "My hello world operation",
        parameters: {
          message: {
            description: "A message to say to the world",
            location: 'query',
            required: true,  
            schema: { type: 'string' }
          }
        }
        service: function(req) {
          return { msg: "Hello World! " + req.parameters.message }
        }
      }
    }

..  code-block:: javascript

    {
      post: {
        description: "Adds a Zipcode object to the zipcodes collection",
        parameters: {
          body: {
            description: "A Zipcode object",
            location: 'body',
            required: true,
            schema: { 
              type: 'object',
              properties: {
                _id: { type: 'number' },
                state: { type: 'string' }
              }
            }
          }
        }
        service: function(req) {
          this.getService().db.getCollection("zipcodes").insert(req.parameters.body)
        } 
      }
    }


Parameter schemas 
-----------------

TODO

Parameter parsing 
-----------------

TODO

Operation responses 
-------------------

TODO

