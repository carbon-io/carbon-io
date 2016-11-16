// example
var carbon = require('carbon-io')
var o  = carbon.atom.o(module).main
var __ = carbon.fibers.__(module).main

__(function() {
  module.exports = o({
    _type: carbon.carbond.Service,
    port: 8888,
    endpoints: {
      'users': o({
        _type: carbon.carbond.Endpoint,
        get: function(req) {
          // get all users
        }
      }),
      'users/:id': o({
        _type: carbon.carbond.Endpoint,
        get: function(req) {
          // get the user
          return getUserById(req.params.id)
        },
        delete: function(req) {
          // delete the user
        }
      }),
    }
  })
})
