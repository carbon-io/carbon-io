====================
carbond.ObjectServer
====================

.. js:class:: ObjectServer(_type, port, endpoints [, description])
    :hidden:

The :js:class:`ObjectServer` class is the top-level class for defining APIs.

Configuration
=============

..  code-block:: javascript

    {
      _type: carbon.carbond.ObjectServer,
      port: <int>,
      description: <string>,
      dbUri: <string>,
      dbUris: [<string>],
      path: <string>,
      processUser: <string>,
      verbosity: <verbosity>,
      authenticator: <Authenticator>,
      endpoints: {
        <path>: <Endpoint>,
        ...
      }
    }


Properties
==========

- ``_type(carbon.carbond.ObjectServer)``
- ``port(number)``: The port to listen on.
- ``description(string)``: A short description of this API.
- ``dbUri(string)``: The URI for the database (e.g.: ``'mongodb://localhost:27017/mydb'``). The server will connect to this database at startup and expose it through the ``db`` property.
- ``path(string)``: The root URL path for this API. All HTTP requests must use this prefix to reach the endpoints of this API. This value defaults to the empty string '' which results in this :js:class:`ObjectServer` being mounted at ``/``.
- ``processUser(string)``: The unix process user you would like the server to run as after binding to ``port``. This is useful when you need to start the process as root to bind to a privileged port but don't want the process to remain running as root.
- ``verbosity(verbosity)``: Controls the logging level. One of (``'debug'`` | ``'info'`` | ``'warn'`` | ``'error'`` | ``'fatal'``). Default: ``'info'``.
- ``authenticator(Authenticator)``: The :js:class:`Authenticator` object for this API. The authenticator is used to authenticate the API user.
- ``endpoints(document)``: A set of :js:class:`Endpoint` definitions. This is an object whose keys are path strings and values are instances of :js:class:`Endpoint`. Each path key will be interpreted as relative to this :js:class:`ObjectServer` path property. These paths can also define variable bindings (e.g. ``orders/:id``).

Methods
=======

TBD

Example
=======

..  code-block:: javascript

    var carbon = require('carbon-io')
    var o = carbon.atom.o(module, true)

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