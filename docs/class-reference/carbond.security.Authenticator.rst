==============================
carbond.security.Authenticator
==============================

.. js:class:: Authenticator()
    :hidden:

An ``Authenticator`` is an abstract class representing a method of authentication. Authenticators implement an ``authenticate`` method which takes a request and returns a user object.  

Properties
==========

_none_
  
Methods
=======

.. js:function:: authenticate(req)

    :param HttpRequest req: the ``HttpRequest`` object to authenticate
    :return object: an object representing the authenticated user

.. js:function:: isRootUser(user)
    
    :param object user: the user object to test for root equivalence
    :return boolean: ``true`` if the supplied user is a root user

.. js:function:: getAuthenticationHeaders()

    :return [string]: - an array of authentication header names