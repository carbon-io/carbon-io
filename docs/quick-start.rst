===========
Quick Start
===========

Creating your first API
=======================

The first step is to create a standard Node.js package:

..  code-block:: sh

    <path-to-your-app>/
        package.json


Your ``package.json`` file should include ``carbon-io``

..  code-block:: sh

    {
        "name": "hello-world",
        "description": "Hello World API",
        "dependencies": {
            "carbon-io" : "> 0.1.0"
        }
    }

Then install the package dependencies like this:

..  code-block:: sh

    % cd <path-to-your-app>
    % npm install

Next we define the API. This is where the magic is. Create a file called HelloService.js:

..  code-block:: sh

    <path-to-your-app>/
      package.json
      HelloService.js


HelloService.js

..  code-block:: javascript

 var carbon = require('carbon-io')
 var o  = carbon.atom.o(module).main
 var __ = carbon.fiber.__(module).main

 __(function() {
   module.exports = o({
     _type: carbon.carbond.Service,
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

.. _quick-start-running-the-api:

Running the API
===============

..  code-block:: sh

 % node <path-to-your-app>/HelloService
 [Mon Feb 09 2015 21:56:41 GMT-0800 (PST)] INFO: Service starting...
 [Mon Feb 09 2015 21:56:41 GMT-0800 (PST)] INFO: Service listening on port 8888
 [Mon Feb 09 2015 21:56:41 GMT-0800 (PST)] INFO: Service started

Connecting to the API
=====================

You now have a RESTful web service running on port 8888. 

..  code-block:: console

 % curl localhost:8888/hello
 { "msg": "Hello world!" }
 %
