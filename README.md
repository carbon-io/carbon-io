Carbon.io
==========
***

Carbon.io is an application framework based on Node.js and MongoDB for building command line programs, microservices, and APIs.

Carbon.io strives to make the simple cases easy and the complex cases possible. With Carbon.io you can create simple, database-centric, APIs with virtually no code. At the same time Carbon.io is designed to let you under the hood and allows you to write highly customized APIs much like you would with lower-level libraries such as Express.js. 

Carbon.io has a highly declarative and modular style that is different from most application programming frameworks and that is quite fun to code in. 

Carbon.io is easy to learn. We recommend starting with the [Quick start](doc/GettingStarted.md) guide and then trying out some of the many examples in our [examples repository](https://github.com/carbon-io/examples). Then dive into the [user guide]() to learn more advanced concepts.

Contents
-------

* [Quick start](doc/GettingStarted.md)
  * [Creating your first API](doc/GettingStarted.md#creating-the-api)
  * [Running the API](doc/GettingStarted.md#running-the-api)
  * [Connecting to the API](doc/GettingStarted.md#connecting-to-the-api)
* [More examples](https://github.com/carbon-io/examples)
* User guides
  * [carbond] (https://github.com/carbon-io/carbond)
  * [carbon-client] (https://github.com/carbon-io/carbon-client)
  * [carbon-shell] (https://github.com/carbon-io/carbon-shell)
  * [atom] (https://github.com/carbon-io/atom)
  * [bond] (https://github.com/carbon-io/bond)
  * [leafnode] (https://github.com/carbon-io/leafnode)



* Installing 
  * Overview
    * Design philosophy 
  * Fundamental technologies
    * Atom
    * Bond
    * Fiber / node-fibers
    * Leafnode 
    * JSON Schema
    * Swagger
 
 
| property      | description     | type  | default |
| :------------ |:----------------| :-----| :-----  |
| port          | Http port server will listen on | number | 8888 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |


Quick start (Hello World)
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
    "engines": { "node": "~0.8.6" },
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
          return { msg: "Hello World!" }
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
   -v VERBOSITY, --verbosity VERBOSITY   verbosity level (trace | debug | info | warn | error | fatal)
   --root-secret-key ROOT_SECRET_KEY     root secret key
```
### Connecting to the API

You now have a RESTful web service running on port 8888. You can connect to it via HTTP in a variety of ways. 

**Simple curl test**

```console
% curl localhost:8888/hello
{ "msg": "Hello World!" }
%
```

**API Browser**

In your web browser navigate to [http://localhost:8888/apidoc](http://localhost:8888/apidoc) to use the auto-generated API Browser. 

![HelloService](./hello-service.png)

### More examples

Studying examples is a great way to learn. We have an entire [github repository full of runnable examples](https://github.com/carbon-io/examples) to explore. 

