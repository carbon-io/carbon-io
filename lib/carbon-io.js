var mongodb = require('leafnode').mongodb

module.exports = {
  atom: require('atom'),
  bond: require('bond'),
  fiber: require('fiber'),
  carbond: require('carbond'),
  testtube: require('test-tube'),
  bson: { // XXX not sure if we want all of these exported, but this is everything mongodb exports from BSON
    Binary: mongodb.Binary,
    Code: mongodb.Code,
    Map: mongodb.Map,
    DBRef: mongodb.DBRef,
    Double: mongodb.Double,
    Long: mongodb.Long,
    MinKey: mongodb.MinKey,
    MaxKey: mongodb.MaxKey,
    ObjectId: mongodb.ObjectId,
    Symbol: mongodb.Symbol,
    Timestamp: mongodb.Timestamp,
    Decimal128: mongodb.Decimal128
  }
}
