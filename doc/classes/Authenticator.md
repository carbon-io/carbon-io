class Authenticator
----------

An ```Authenticator``` is an abstract class representing a method of authentication. Authenticators implement an ```authenticate``` method which takes a request and returns a user object.  

Properties
----------

_none_

Methods
----------

#### authenticate(req)

**Parameters**
* ```req``` - the ```HttpRequest``` object to authenticate

**Returns** (```object```) - an object representing the authenticated user

#### isRootUser(user)

**Parameters**
* ```user``` (```object```) - the user object to test for root equivalence 

**Returns** (```boolean```) - ```true``` iff the supplied user is a root user

#### getAuthenticationHeaders()

**Parameters**

**Returns** ```[string]``` - an array of authenication header names
