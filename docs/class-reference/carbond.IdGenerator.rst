===================
carbond.IdGenerator
===================

.. js:class:: IdGenerator()
    :hidden:

An ``IdGenerator`` is an abstract class representing a method of ``_id`` generation. ``IdGenerator``\ s have  
a ``generateId`` method which concrete classes must implement. ``IdGenerator``\ s may generate values of any type.

Properties
==========

_none_

Methods
==========

.. js:function:: generateId()

    :return (any): A value.