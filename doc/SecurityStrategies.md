Security strategies
----------

When creating APIs there are two general strategies one can take towards security. One strategy is to implement security implicity, by virtue of the way the code is written. The other is to use more explicit definitions of access control to define user permissions on endpoints and data. 

The two strategies can, and often are, combined within the same API having Endpoints that use varying techniques. 

Both techniques rely on Object Server [authentication](Authentication.md). 

### Implicit Security

Implicit security is a strategy that most resembles the way security is implemented in traditional server-side MVC applications. With this strategy, each operation is written in such a way that the authenticated user cannot access data in a way that is disallowed. 

For example, a ```/contacts``` endpoint meant to retrieve the all the ```Contact```s for the currently authenticated user might be written as:

```
var userId = req.user._id
var contacts = lookupContactsInDatabaseByUserId(userId)
res.send(user)
```

where ```lookupContactsInDatabaseByUserId``` does what you would expect as well as properly curates which fields should be returned. 

With this code it would be impossible for the authenticated user to retrieve data associated with another user. 

### Explicit Security

Explicit security relies on ACLs defined on endpoints and data to describe what permissions users have and automatically enforce those permissions. Using this technique often involves less code and more configuration. 

For example, a ```/users/:userId/contacts``` endpoint meant to retrieve the all the ```Contact```s the currently authenticated user has permission to see might be written as:

```
TODO
```
