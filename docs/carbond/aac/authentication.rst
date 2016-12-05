==============
Authentication
==============

.. toctree::

A ``Service`` accomplishes user authentication via ``Authenticator``
components which are responsible for associating incoming requests
with users.

Every ``Service`` can be configured with an ``Authenticator``. When so
configured, the ``Service`` will dispatch each HTTP request to that
``Authenticator``\'s ``authenticate(req)`` method. This method will
use credentials in the request (e.g. HTTP Basic credentials, API-key,
etc...) to authenticate and return the user associated with those
credentials, if one exists. The ``Service`` will then store the
resolved user object in the ``HttpRequest`` object.

The user associated with the request can later be accessed via the
``user`` property of the request (e.g. ``req.user``).


Built-in authenticators
-----------------------

Carbond comes with several out-of-the-box ``Authenticator``\s:

* ``HttpBasicAuthenticator`` - Base class for implementing HTTP basic
  authentication.
* ``MongoDBHttpBasicAuthenticator`` - An ``HttpBasicAuthenticator`` backed by MongoDB. 
* ``ApiKeyAuthenticator`` - Base class for implementing API-key based
  authentication.
* ``MongoDBApiKeyAuthenticator`` - An ``ApiKeyAuthenticator`` backed
  by MongoDB.
* ``OauthAuthenticator`` *(not yet implemented)*


Custom Authenticators 
---------------------

You can define your own custom ``Authenticator``\s by creating an
instance of ``Authenicator`` (or a subclass) with a custom
``authenticate`` method.

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 5

  o({
    _type: carbon.carbond.security.Authenticator,
    
    authenticate: function(req) {
      var user = figureOutWhoUserIs();
      return user;
    }
  })

Examples
--------

**HTTP Basic authentication**

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 4 - 9, 14

  module.exports = o({
    _type: carbon.carbond.Service,
    port: 8888,
    authenticator: o({
      _type: carbon.carbond.security.MongoDBHttpBasicAuthenticator,
      userCollection: "users",
      usernameField: "username",
      passwordField: "password"
    }),      
    endpoints: {
      hello: o({
        _type: carbon.carbond.Endpoint,
        get: function(req) {
          return { msg: "Hello " + req.user.email}
        }
      })
    }
  })

**API Key authentication**

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 4 - 10, 15

  module.exports = o({
    _type: carbon.carbond.Service,
    port: 8888,
    authenticator: o({
      _type: carbon.carbond.security.MongoDBApiKeyAuthenticator,
      apiKeyParameterName: "API_KEY",
      apiKeyLocation: "header", // can be "header" or "query"
      userCollection: "users",
      apiKeyUserField: "apiKey"
    }),
    endpoints: {
      hello: o({
        _type: carbon.carbond.Endpoint,
        get: function(req) {
          return { msg: "Hello " + req.user.email}
        }
      })
    }
  })

**Custom authentication**

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 4 - 10, 15

  module.exports = o({
    _type: carbon.carbond.Service,    
    port: 8888,
    authenticator: o({
      _type: carbon.carbond.security.Authenticator,
      authenticate: function(req) {
        var user = figureOutWhoUserIs();
        return user;
      }
    }),
    endpoints: {
      hello: o({
        _type: carbon.carbond.Enpoint,
        get: function(req) {
          return { msg: "Hello " + req.user.email}
        }
      })
    }
  })
