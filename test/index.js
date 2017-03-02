var o = require('@carbon-io/atom').o(module).main
var _o = require('@carbon-io/bond')._o(module)
var testtube = require('@carbon-io/test-tube')

module.exports = o({
  _type: testtube.Test,
  name: 'CarbonCoreTests',
  tests: [require('@carbon-io/carbon-core').$Test,
          require('@carbon-io/carbond').$Test]
})
