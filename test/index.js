var __ = require('@carbon-io/carbon-core').fibers.__(module)
var o = require('@carbon-io/atom').o(module)
var _o = require('@carbon-io/bond')._o(module)
var testtube = require('@carbon-io/test-tube')

__(function() {
  module.exports = o.main({
    _type: testtube.Test,
    name: 'CarbonIoTests',
    tests: [
      require('@carbon-io/carbon-core').$Test,
      require('@carbon-io/carbond').$Test
    ]
  })
})
