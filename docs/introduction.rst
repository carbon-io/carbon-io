.. _carbon-io-intro: 

============
Introduction
============

Carbon.io is an application framework based on Node.js and MongoDB for
building APIs and microservices.

Carbon.io strives to make the simple cases easy and the complex cases
possible. With Carbon.io you can create simple, database-centric
microservices with virtually no code. At the same time Carbon.io is
designed to let you under the hood and allows you to write highly
customized APIs much like you would with lower-level libraries such as
Express.js.

For instance, this example creates a full CRUD API for single MongoDB
collection consisting of eight REST operations with 'no code':

.. code-block:: javascript    

 __(function() {
   module.exports = o({
     _type: carbon.carbond.Service,
     port: 8888,
     dbUri: 'mongodb://localhost:27017/mydb',
     endpoints: {
       zipcodes: o({
         _type: carbon.carbond.mongodb.MongoDBCollection,
         collection: 'zipcodes'
       })
     }
   })
 })

When run, this service exposes the following:

* ``/zipcodes`` (``GET``, ``POST``, ``PATCH``, ``DELETE``)
* ``/zipcodes/:id`` (``GET``, ``POST``, ``PUT``, ``DELETE``)
 
In other use cases you may need a lot of lower-level control over how
your endpoints are implemented. Carbon.io let's you do this too:

.. code-block:: javascript    

   __(function() {
     module.exports = o({
       _type: carbon.carbond.Service,
       port: 8888,
       dbUri: 'mongodb://localhost:27017/mydb',
       endpoints: {
         zipcodes: o({
           _type: carbon.carbond.Endpoint,
           get: function(req, res) {
             // connect to legacy COBOL program from 1987 using some random Node.js
             // library you found on npm. 
           },
           post: function(req, res) {
             ...
           },
           ...
         })
       }
     })
   })

In addition to helping you build endpoints, Carbon.io also takes care
of a lot of the common infrastructure one commonly has to implement
when building a mircoservice or API, such as:

- Authentication and access control
- Parameter parsing and validation
- HTTP status code and error handling
- Logging
- Unit testing
- Documentation

Carbon.io has a highly declarative and modular style that is different
from most application programming frameworks and that is quite fun to
code in and easy to learn. We recommend starting with the :ref:`quick
start guide <carbon-io-quick-start>` and then trying out some of the many
examples in our :ref:`examples <carbon-io-examples>` section. Then dive
into the :ref:`server guide <carbond-server-guide>` to learn more
advanced concepts.
