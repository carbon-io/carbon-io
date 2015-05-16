Carbon.io
==========
***

Contents
-------

* [Overview](#overview)
* [Quick start](doc/GettingStarted.md)
  * [Creating your first API](doc/GettingStarted.md#creating-the-api)
  * [Running the API](doc/GettingStarted.md#running-the-api)
  * [Connecting to the API](doc/GettingStarted.md#connecting-to-the-api)
* [Carbon.io example repository](https://github.com/carbon-io/examples)
* [User guides](#user-guides)
  * [carbond] (https://github.com/carbon-io/carbond): The server component of Carbon.io. This is how you build APIs and microservices.
  * [carbon-client] (https://github.com/carbon-io/carbon-client): The client component to Carbon.io. This is how you talk to APIs and microservices.
  * [carbon-shell] (https://github.com/carbon-io/carbon-shell): A command-line shell you can use to connect to and interact with Carbond servers.
  * [atom](https://github.com/carbon-io/atom): The core component framework upon which Carbon.io is built.
  * [bond](https://github.com/carbon-io/bond): The Carbon.io name resolver.
  * [fiber](https://github.com/carbon-io/fiber): The Carbon.io interface to [Node Fibers](https://github.com/laverdet/node-fibers) used for synchronous control flow. 
  * [leafnode](https://github.com/carbon-io/leafnode): A hybrid synchronous / asynchronous MongoDB driver interface (wraps the [node-mongodb-native](https://github.com/mongodb/node-mongodb-native) driver). 
* Design philosophy
* FAQ
 
Overview
----------

Carbon.io is an application framework based on Node.js and MongoDB for building command line programs, microservices, and APIs.

Carbon.io strives to make the simple cases easy and the complex cases possible. With Carbon.io you can create simple, database-centric, microservices with virtually no code. At the same time Carbon.io is designed to let you under the hood and allows you to write highly customized APIs much like you would with lower-level libraries such as Express.js. 

For instance, this example creates a full CRUD API for single MongoDB collection consisting of six REST endpoints with 'no code': 
```node
__(function() {
  module.exports = o({
    _type: carbon.carbond.ObjectServer,
    port: 8888,
    endpoints: {
      zipcodes: o({
        _type: carbon.carbond.MongoDBCollection,
        collection: 'zipcodes'
      })
    }
  })
})
```

But sometimes you need to go to town with very custom code. Carbon.io let's you do this too with no restrictions and lets you write the code you need to write:

```node
__(function() {
  module.exports = o({
    _type: carbon.carbond.ObjectServer,
    port: 8888,
    endpoints: {
      zipcodes: o({
        _type: carbon.carbond.Endpoint,
        get: function(req, res) {
          // connect to legacy COBOL program from 1987 using some crazy library
          // written by a guy in Belarus 
        },
        post: function(req, res) {
          ...
        },
        ...
      })
    }
  })
})
```

In addition to helping you build endpoints, Carbon.io also takes care of a lot of the common infrastructure one commonly has to implement when building a mircoservice or API, such as:

* Logging
* Proper HTTP error handling
* Authentication and access control
* Application configuration and bootstrapping
* Building robust command-line interfaces
* JSON-Schema validation
* API documentation (auto-generated)

Carbon.io has a highly declarative and modular style that is different from most application programming frameworks and that is quite fun to code in and easy to learn. We recommend starting with the [Quick start](doc/GettingStarted.md) guide and then trying out some of the many examples in our [examples repository](https://github.com/carbon-io/examples). Then dive into the [user guide]() to learn more advanced concepts.

Quick start (Hello world)
----------

### Creating your first API

The first step is to create a standard Node.js package

```
<path-to-your-app>/
    package.json
```

Your ```package.json``` file should include ```carbon-io```

```node
{
    "name": "hello-world",
    "description": "Hello World API",
    "dependencies": {
        "carbon-io" : "> 0.1.0"
    }
}
```

Then install the package dependencies like this:

```console
% cd <path-to-your-app>
% npm install .
```

Next we define the API. This is where the magic is. Create a file called HelloService.js:

```
<path-to-your-app>/
    package.json
    HelloService.js
```

HelloService.js
```node
var carbon = require('carbon-io')
var o  = carbon.atom.o(module)
var __ = carbon.fiber.__(module, true)

__(function() {
  module.exports = o({
    _type: carbon.carbond.ObjectServer,
    port: 8888,
    endpoints: {
      hello: o({
        _type: carbon.carbond.Endpoint,
        get: function(req) {
          return { msg: "Hello world!" }
        }
      })
    }
  })
})
```

### Running the API

```console
% node <path-to-your-app>/HelloService
[Mon Feb 09 2015 21:56:41 GMT-0800 (PST)] INFO: ObjectServer starting...
[Mon Feb 09 2015 21:56:41 GMT-0800 (PST)] INFO: ObjectServer listening on port 8888
[Mon Feb 09 2015 21:56:41 GMT-0800 (PST)] INFO: ObjectServer started
```

command help
```console
% node <path-to-your-app>/HelloService -h
Usage: node HelloService [options]

Options:
   -p PORT, --port PORT                  port
   -v VERBOSITY, --verbosity VERBOSITY   verbosity level (trace | debug | info | warn | error)
```
### Connecting to the API

You now have a RESTful web service running on port 8888. You can connect to it via HTTP in a variety of ways. 

**Simple curl test**

```console
% curl localhost:8888/hello
{ "msg": "Hello world!" }
%
```

**API Browser**

In your web browser navigate to [http://localhost:8888/apidoc](http://localhost:8888/apidoc) to use the auto-generated API Browser. 

![HelloService](doc/hello-service.png)

Carbon.io example repository
----------

Studying examples is a great way to learn. We have an entire [github repository full of runnable examples](https://github.com/carbon-io/examples) to explore. 

User guides
----------
* [carbond] (https://github.com/carbon-io/carbond): The server component of Carbon.io. This is how you build APIs and microservices. Start here.
* [carbon-client] (https://github.com/carbon-io/carbon-client): The client component to Carbon.io. This is how you talk to APIs and microservices.
* [carbon-shell] (https://github.com/carbon-io/carbon-shell): A command-line shell you can use to connect to and interact with Carbond servers.
* [atom](https://github.com/carbon-io/atom): The core component framework upon which Carbon.io is built.
* [bond](https://github.com/carbon-io/bond): The Carbon.io name resolver.
* [fiber](https://github.com/carbon-io/fiber): The Carbon.io interface to [Node Fibers](https://github.com/laverdet/node-fibers) used for synchronous control flow. 
* [leafnode](https://github.com/carbon-io/leafnode): A hybrid synchronous / asynchronous MongoDB driver interface (wraps the [node-mongodb-native](https://github.com/mongodb/node-mongodb-native) driver). 

Design philosophy
----------

_TODO_

FAQ
----------

_TODO_
