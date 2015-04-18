Authentication
----------

An Object Server accomplishes user authentication via ```Authenticator``` components which are responsible for associating incoming requests with users.

Every Object Server can be configured with an ```Authenticator```. When so configured, the Object Server will dispatch each HTTP request to that ```Authenticator```'s ```authenticate(req)``` method. This method will use credentials in the request (e.g. HTTP Basic credentials, API-key) to authenticate and return the user associated with those credentials, if one exists. The Object Server will then store the resolved user object in the ```HttpRequest``` object. 

The user associated with the request can later be accessed via the ```user``` property of the request like so:

```
req.user
```

Datanode comes with several out-of-the-box ```Authenticator```s:

* An ```HttpBasicAuthenticator```
* An ```ApiKeyAuthenticator``` 
* An ```OauthAuthenticator``` _(not yet implemented)_

Furthemore, custom ```Authenticator```s can be defined by subclassing existing ```Authenticator``` classes.

Custom Authenticators
----------

You can define your own custom ```Authenticator```s by creating an instance of ```Authenicator``` (or a subclass) with a custom ```authenticate``` method.  

```node
o({
  _type: 'datanode/Authenticator',
  
  authenticate: function(req) {
    var user = figureOutWhoUserIs();
    return user;
  }
})
```

Examples
----------

HTTP Basic authentication
```node
var o = require('maker').o(module)

module.exports = o({
  _type: 'datanode/ObjectServer',
  port: 8888,
  authenticator: o({
    _type: 'datanode/security/MongoDBHttpBasicAuthenticator',
    userCollection: "users",
    usernameField: "username",
    passwordField: "password"
  }),
  
  endpoints: {
    hello: o({
      _type: 'datanode/Endpoint',
      get: function(req) {
        return { msg: "Hello " + req.user.email}
      }
    })
  }
})
```

API Key authentication
```node
var o = require('carbon').atom.o(module)

module.exports = o({
  _type: 'datanode/ObjectServer',
  port: 8888,
  authenticator: o({
    _type: 'datanode/security/MongoDBApiKeyAuthenticator',
    apiKeyParameterName: "API_KEY",
    apiKeyIn: "header", // can be "header" or "query"
    userCollection: "users",
    apiKeyUserField: "apiKey"
  }),
  endpoints: {
    hello: o({
      _type: 'datanode/Endpoint',
      get: function(req) {
        return { msg: "Hello " + req.user.email}
      }
    })
  }
})
```

Custom authentication
```node
var o = require('carbon').bond.o(module)

module.exports = o({
  _type: 'datanode/ObjectServer',
  
  port: 8888,
  
  authenticator: o({
    _type: 'Authenticator',
    authenticate: function(req) {
      var user = figureOutWhoUserIs();
      return user;
    }
  }),
  
  endpoints: {
    hello: o({
      _type: 'datanode/Endpoint',
      get: function(req) {
        return { msg: "Hello " + req.user.email}
      }
    })
  }
})
```
