Access Control
----------

The Object Server accomplishes access control by way of ACLs or _Access Control Lists_. 

There are two types of ACLs
* Endpoint ACLs
* Object ACLs

ACLs
----------

ACL objects are comprised of:

* ```permissionDefinitions``` - This defines the set of permissions that can be used in this ACL by mapping default permission names, as ```string```s, to default values in the form of _permission predicates_. Permission predicates are either simple boolean values or a function that takes a user object and returns a boolean value. 

* ```groupDefinitions``` - This defines the set of group names that will be used in the ACL. Each entry defines a group by mapping it to a property path, as a ```string```, or a function that takes a user and returns a value. If provided with a property path the path is evaluated against the authenticated user when checking ACL permissions. By default there always exists a group with the name ```user``` to allow for individual users to be specified in ACL entries. 

* ```entries``` - This defines the actual access control list for the ACL as a mapping of _user specifiers_ to a set of _permissions_. Each user specifier is a ```string``` of the form ```<group-name>:<value>``` where ```group-name``` is one of the groups defined in ```groupDefinitions```. Each permission object is a mapping of a permisson (defined in ```permissionDefinitions```) to a _permission predicate_. Permission predicates are either simple boolean values or a function that takes a user object and returns a boolean value. 

```node
{
  permissionDefinitions: { // map of permissions to defaults boolean values
    <string>: <permission-predicate>(boolean | function)
  },
  
  groupDefinitions: {
    <string>: <string> // map of group names to property paths (or function(user) --> value )
  },
  
  entries: { // actual ACL entries 
    <user-specifier(string)>: { // map of user specifier to list of permissions
      <permission(string)>: <permission-predicate>(boolean | function)>
    }
  }
}
```

### Example
```node
{
  permissionDefinitions: { // This ACL has two permissions, read and write
    read: false,
    write: false
  },
  
  groupDefinitions: { // This ACL defines three groups, role, title, and region
    role: 'role',
    title: function(user) { return user.title; },
    region: 'address.zip'
  },
  
  entries: {  
    'role:"Admin"': {
      "*": true
    },
    'title:"CFO"': {
      read: true,
      write: true
    },
    'user:1234': {
      read: true,
      write: false
    }
  }
}
```
