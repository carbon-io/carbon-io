==============
Error handling
==============

.. toctree::

HTTP errors can be thrown as exceptions from within your code to
communicate HTTP errors to clients of your ``Service``. 

For example, the following will produce an HTTP ``400`` error (Bad Request):

..  code-block:: javascript 
  :linenos:
  :emphasize-lines: 14

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
          post: function(req) {
            if (!req.body) {
              throw new carbon.HttpErrors.BadRequest("Must supply a body")
            }
            return { msg: "Hello World! " + req.body }
          }
        }) 
      }
    }) 
  })

**Supported HTTP errors**

* ``400``: BadRequest
* ``401``: Unauthorized
* ``402``: PaymentRequired
* ``403``: Forbidden
* ``404``: NotFound
* ``405``: MethodNotAllowed
* ``406``: NotAcceptable
* ``407``: ProxyAuthenticationRequired
* ``408``: RequestTimeout
* ``409``: Conflict
* ``410``: Gone
* ``411``: LengthRequired
* ``412``: PreconditionFailed
* ``413``: RequestEntityTooLarge
* ``414``: RequestURITooLarge
* ``415``: UnsupportedMediaType
* ``416``: RequestedRangenotSatisfiable
* ``417``: ExpectationFailed
* ``418``: ImATeapot
* ``421``: MisdirectedRequest
* ``422``: UnprocessableEntity
* ``423``: Locked
* ``424``: FailedDependency
* ``426``: UpgradeRequired
* ``428``: PreconditionRequired
* ``429``: TooManyRequests
* ``431``: RequestHeaderFieldsTooLarge
* ``500``: InternalServerError
* ``501``: NotImplemented
* ``502``: BadGateway
* ``503``: ServiceUnavailable
* ``504``: GatewayTimeOut
* ``505``: HTTPVersionNotSupported
* ``506``: VariantAlsoNegotiates
* ``507``: InsufficientStorage
* ``508``: LoopDetected
* ``510``: NotExtended
* ``511``: NetworkAuthenticationRequired
