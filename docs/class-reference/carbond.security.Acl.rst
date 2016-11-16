====================
carbond.security.Acl
====================

TODO

Old (for class ref) 
------------- 
ACL objects are comprised of:

- ``permissionDefinitions`` - This defines the set of permissions that can be used in this ACL by mapping default permission names, as ``strings``, to default values in the form of *permission predicates*. Permission predicates are either simple boolean values or a function that takes a user object and returns a boolean value. 

- ``groupDefinitions`` - This defines the set of group names that will be used in the ACL. Each entry defines a group by mapping it to a property path, as a ``string``, or a function that takes a user and returns a value. If provided with a property path the path is evaluated against the authenticated user when checking ACL permissions. By default there always exists a group with the name ``user`` to allow for individual users to be specified in ACL entries. 

- ``entries`` - This defines the actual access control list for the ACL as an array of *entry* objects each having a *user specifier* and a set of *permissions*. Each user specifier is either of the form ``user: <userId>`` or of the form ``user: {<group-name>: <value>}`` where ``group-name`` is one of the groups defined in ``groupDefinitions``. Each permission object is a mapping of a permisson (defined in ``permissionDefinitions``) to a *permission predicate*. Permission predicates are either simple boolean values or a function that takes a user object and returns a boolean value. 

..  code-block:: javascript 

    {
      permissionDefinitions: { // map of permissions to defaults boolean values 
        <string>: <permission-predicate>(boolean | function) 
      },
      
      groupDefinitions: {
        <string>: <string> // map of group names to property paths (or function(user) --> value ) 
      },
      
      entries: [ // actual ACL entries 
        {
          user: <user-spec> { 
          permissions: { 
            <permission>: <function> | <boolean>
          }
        }
      ]
    }

**Example**

..  code-block:: javascript 

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
      
      entries: [
        {
          user: { role: "Admin" },
          permissions: {
            "*": true 
          }
        },
        {
          user: { title: "CFO" },
          permissions: {
            read: true,
            write: true 
          }
        },
       {
          user: 1234,
          permissions: {
            read: true,
            write: false 
          }
        }
      ]
    }
