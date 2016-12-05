=====================
Application structure
=====================

*LAST PASS 2016.07.03 HOW DO I GET THAT REF AT BOTTOM TO WORK?*

Defining your Node.js package 
-----------------------------

To build a Carbon.io service you start by creating a standard node package:

..  code-block:: sh

 <path-to-your-app>/
     package.json


Your ``package.json`` file should include ``carbon-io``

..  code-block:: sh

 {
   "name": "hello-world",
   "description": "Hello World API",
   "dependencies": {
     "carbon-io" : "> 0.1.0"
   }
 }

You then install the package dependencies like so

..  code-block:: sh

 % cd <path-to-your-app>
 % npm install .

Defining your Service 
---------------------

Next you create your app / service. All ``carbond`` services will have the same top-level structure

..  code-block:: sh

 <path-to-your-app>/
     package.json
     MyService.js

In ``MyService.js``:

..  code-block:: javascript

 var carbon = require('carbon-io')
 var o  = carbon.atom.o(module).main
 var __ = carbon.fibers.__(module).main
 var _o = carbon.bond._o(module)

 __(function() {
   module.exports = o({
     _type: carbon.carbond.Service,
     .
     .
     .
     // implementation of your service goes here
     .
     .
     .
   })
 })

Using o, __, and _o
--------------------

The preamble requires the main ``carbon-io`` package as well as
defines the ``o``, ``__``, and ``_o`` operators. 

..  code-block:: javascript

    var carbon = require('carbon-io')
    var o  = carbon.atom.o(module).main
    var __ = carbon.fibers.__(module).main
    var _o = carbon.bond._o(module)

The ``o`` operator is part of the Atom sub-project of Carbon.io and 
is what is used to define Carbon.io components. It is not crucial you
understand this deeply at this point but you should eventually read
the `Atom <https://github.com/carbon-io/atom>`_ documentation to
understand the Carbon.io component infrastructure, as it is core to
Carbon.io.

The ``__`` is used to run this service inside of a `Fiber
<https://github.com/carbon-io/fibers>`_ when this module is invoked as
the main module from the command line. Carbon.io makes heavy use of
`Node Fibers <https://github.com/laverdet/node-fibers>`_ to allow for
services to be written in a synchronous (as well as asynchronous)
style. More details can be found in the documentation for the
Carbon.io `fibers package <https://github.com/carbon-io/fibers>`_.

The ``_o`` is the name resolver utility used by Carbon.io. It is not
used in this example, although it is used commonly, and documented as
part of the `bond <https://github.com/carbon-io/bond>`_ sub-project.

Finally, we define our top-level component and export it via
``module.exports``. While exporting the component we define is not
strictly required if we only plan to use this service as a main
module, it is useful to export it so that it can later be required as
a library by other components or modules if desired.

The component is defined to be an instance of the ``carbond.Service``
class which, as we describe in the next section, is the top-level
class used for defining services in ``carbond``.

..  code-block:: javascript

 module.exports = o({
   _type: carbon.carbond.Service
   .
   .
   .
 })

Running your Service 
--------------------

Your top-level ``MyService.js`` file creates a top-level executable application that you can
invoke directly at the command line. 

..  literalinclude:: /frags/shell-output-starting-service.rst
    :language: sh 

For more details on running carbond services see
:doc:`/carbond/running-the-objectserver`

For more details on running carbond services see
:doc:`/carbond/services#running-services-from-the-command-line`

