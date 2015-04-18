class ObjectServer
----------

The ```ObjectServer``` class is the top-level class for defining APIs. 

```node
{
  _type: 'datanode/ObjectServer',
  port: <int>,
  description: <string>,
  dbUri: <string>,
  path: <string>,
  authenticator: <Authenticator>,
  endpoints: {
    <string>: <Endpoint>,
    ...
}
```

Properties
----------

* ```port``` - the port to listen on

* ```description``` - a short description of this API

* ```dbUri``` - the URI for the database (e.g.: ```'mongodb://localhost:27017/mydb' ```). The server will connect to this database at startup and expose it through the ```db``` property

* ```path``` - the root URL path for this API. All HTTP requests must use this prefix to reach the endpoints of this API. This value defaults to the empty string ```''``` which results in this ```ObjectServer``` being mounted at ```/```

* ```authenticator``` - the ```Authenticator``` object for this API. The authenticator is used to authenticate the API user

* ```endpoints``` - an set of ```Endpoint``` definitions. This is an object whose keys are path strings and values are instances of ```Endpoint```. Each path key will be interpreted as relative to this ```ObjectServer```s ```path``` property. These paths can also define variable bindings (e.g. ```orders/:id```)  

Methods
----------

TBD


Example
----------

```node
var o = require('maker').o(module, true)

module.exports = o({
  _type: 'datanode/ObjectServer',
  port: 8888,
  endpoints: {
    hello: o({
      _type: 'datanode/Endpoint',
      get: function(req) {
        return { msg: "Hello World!" }
      }
    })
  }
})
```


