===========
Collections
===========

.. toctree::

Carbond ``Collection``\ s provide a high-level abstraction for
defining ``Endpoint``\s that behave like a collection of
resources. When you define a ``Collection`` you may define the
following methods:

- ``insert(obj, reqCtx)``
- ``find(query, options, reqCtx)``
- ``update(query, obj, options, reqCtx)``
- ``remove(query, reqCtx)``
- ``getObject(id, reqCtx)``
- ``updateObject(id, reqCtx)``
- ``removeObject(id, reqCtx)``

Which results in the following tree of ``Endpoint``\s and ``Operation``\s:

- ``/<collection>``

  - ``GET`` which maps to ``find``
  - ``POST`` which maps to ``insert``
  - ``PUT`` which maps to ``update``
  - ``DELETE`` which maps to ``remove``
    
- ``/<collection>/:id``

  -  ``GET`` which maps to ``getObject``
  -  ``PUT`` which maps to ``updateObject``
  -  ``DELETE`` which maps to ``removeObject``

.. _Collections: https://mongolab.com/

When defining a Collections_ one is not required to define all methods. Only defined methods will be enabled. For example, here is a collection that only defines the ``insert`` method:

..  code-block:: javascript

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      dbUri: "mongodb://localhost:27017/mydb",
      endpoints: {
        feedback: o({
          _type: carbon.carbond.collections.Collection,
          // POST /feedback
          insert: function(obj) {
            return this.service.db.getCollection('feedback').insert(obj)
          }
        })
      }
    })
  })
