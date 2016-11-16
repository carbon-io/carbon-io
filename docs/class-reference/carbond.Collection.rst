==================
carbond.Collection
==================

.. js:class:: Collection()
    :hidden:

Carbond ``Collection``\ s provide a high-level abstraction for defining ``Endpoint``\ s that behave like a collection of 
resources. When you define a ``Collection`` you define the following methods:

- ``insert(obj, reqCtx)``
- ``find(query, options, reqCtx)``
- ``update(query, obj, options, reqCtx)``
- ``remove(query, reqCtx)``
- ``findObject(id, reqCtx)``
- ``updateObject(id, reqCtx)``
- ``removeObject(id, reqCtx)``

Which results in the following tree of ``Endpoints`` and ``Operations``:

- ``/<collection>``

  - ``GET`` which maps to ``find``
  - ``POST`` which maps to ``insert``
  - ``PUT`` which maps to ``update``
  - ``DELETE`` which maps to ``remove``
    
- ``/<collection>/:id``

  -  ``GET`` which maps to ``findObject``
  -  ``PUT`` which maps to ``updateObject``
  -  ``DELETE`` which maps to ``removeObject``


Configuration
=============

..  code-block:: javascript

    {
      _type: carbon.carbond.Collection, // extends Endpoint
      
      [parameters: {
        <name> : <OperationParameter>
      }]  
      
      [insert: <function>],
      [find: <function>],
      [update: <function>],
      [remove: <function>],
      [findObject: <function>],
      [updateObject: <function>],
      [removeObject: <function>]
      
      [endpoints: { 
        <path>: <Endpoint>
        ...
      }]
    }

Properties
==========

- ``path`` (read-only): The path to which this ``Collection`` is bound. The path can contain variable patterns (e.g. ``'orgs/:id/members'``). The ``path`` property is not configured directly on ``Collection`` objects but are specified as lvals in enclosing definitions of endpoints such as in an ``ObjectServer`` or a parent ``Endpoint`` object. When retrieved the value of this property will be the absolute path of the endpoint from ``/``. 

- ``parent`` (read-only): The parent ``Endpoint`` of this ``Collection``.

- ``objectserver`` (read-only): The ``ObjectServer`` to which this endpoint belongs.

- ``parameters``: A mapping of parameter names to ``OperationParameter`` objects. Parameters defined for an ``Endpoint`` are inherited by all operations of this ``Endpoint`` as well as by all child ``Endpoint``\ s of this ``Endpoint``.

- ``endpoints``: A set of child ``Endpoint`` definitions. This is an object whose keys are path strings and values are instances of ``Endpoint``. Each path key will be interpreted as relative to this ``Endpoint``\ s ``path`` property. 

Methods
=======

_TBD_

RESTFul interface
=================

- ``/<collection>``
  
  - ``GET`` which maps to ``find``
  - ``POST`` which maps to ``insert``
  - ``PUT`` which maps to ``update``
  - ``DELETE`` which maps to ``remove``
    
- ``/<collection>/:id``
  
  -  ``GET`` which maps to ``findObject``
  -  ``PUT`` which maps to ``updateObject``
  -  ``DELETE`` which maps to ``removeObject``

Examples (synchronous)
----------------------

..  code-block:: javascript

    __(function() {
      module.exports = o({
        _type: carbon.carbond.ObjectServer,
        port: 8888,
        dbUri: "mongodb://localhost:27017/mydb",
        endpoints: {
          feedback: o({
            _type: carbon.carbond.Collection,
            insert: function(obj) {
              return this.objectserver.db.getCollection('feedback').insert(obj)
            }
          })
        }
      })
    })
