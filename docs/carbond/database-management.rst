===================
Database management
===================

.. toctree::

Carbond makes it easy to manage connections to multiple databases in
your application. The ``Service`` class has two properties for
specifying database URIs:

- ``dbUri``: A connection string specified as a `MongoDB URI
  <http://docs.mongodb.org/manual/reference/connection-string/>`_
  (e.g. ``"mongodb:username:password@localhost:27017/mydb"``). The
  ``Service`` will connect to this database on startup. The
  application can then reference a connection to this database via the
  ``db`` property on the ``Service``.

- ``dbUris``: A mapping of names to `MongoDB URIs
  <http://docs.mongodb.org/manual/reference/connection-string/>`_. The
  ``Service`` will connect to these databases on startup. The
  application can reference a connection to these databases via the
  ``Service`` as ``dbs[<name>]`` or ``dbs.<name>``.

**Examples**

A ``Service`` with a single db connection:

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 5, 10

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      dbUri: "mongodb://localhost:27017/mydb",
      endpoints: {
        hello: o({
          _type: carbon.carbond.Endpoint,
          get: function(req) {
            return this.getService().db.getCollection('messages').find().toArray()
          }
        })
      }
    })
  })

A ``Service`` that connects to multiple databases:

..  code-block:: javascript
  :linenos:
  :emphasize-lines: 5-8, 13, 19

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      dbUris: {
        main: "mongodb://localhost:27017/mydb",
        reporting: "mongodb://localhost:27017/reporting"
      }
      endpoints: {
        messages: o({
          _type: carbon.carbond.Endpoint,
          get: function(req) {
            return this.getService().dbs['main'].getCollection('messages').find().toArray()
          }
        }),
        dashboards: o({
          _type: carbon.carbond.Endpoint,
          get: function(req) {
            return this.getService().dbs['reporting'].getCollection('dashboards').find().toArray()
          }
        })
      }
    })
  })
