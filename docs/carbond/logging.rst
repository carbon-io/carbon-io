=======
Logging
=======

.. toctree::

The ``Service`` class provides a logging facility that can be used to
log application messages at various logging levels. 

Logging messages 
----------------

To support logging the ``Service`` class exposes the following
methods:

* ``logTrace(msg)`` 
* ``logDebug(msg)`` 
* ``logInfo(msg)`` 
* ``logWarning(msg)`` 
* ``logError(msg)`` 
* ``logFatal(msg)`` 

To log a message you simply use these methods on your ``Service``
object:

..  code-block:: javascript 
  :linenos:
  :emphasize-lines: 13, 17

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module).main 
  var __ = carbon.fibers.__(module).main

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      endpoints: {
        hello: o({
          _type: carbon.carbond.Endpoint,
          get: function(req) {
            this.getService().logInfo("GET on /hello called")
            try {
              // Do stuff
            } catch (e) {
              this.getService().logError("Error while doing stuff")
            }
            return { msg: "Hello World!" }
          }
        }) 
      }
    }) 
  })

Controling verbosity 
--------------------

The verbosity level of your ``Service`` at runtime (i.e. which log
levels are logged) can is controlled by the ``verbosity`` property of
you ``Service`` object. 

The verbosity property is a string and can have the following values:

* ``'trace'``
* ``'debug'``
* ``'info'``
* ``'warn'``
* ``'error'``
* ``'fatal'``

These values have an ordering, and by setting the ``verbosity``
property to one of these values you are directing the ``Service`` to
log all messages with that log level and any "higher" log level. 

For example, setting the ``verbosity`` to ``'info'`` will result in all
messages of log level ``'info'``, ``'warn'``, ``'error'``, and ``'fatal'`` to
be logged. 

There are two ways to control the verbosity level of a ``Service``:

1. Setting the ``verbosity`` property of the ``Service`` as part of its
   configuration:

.. code-block:: javascript 
  :linenos:
  :emphasize-lines: 9 

  var carbon = require('carbon-io') 
  var o  = carbon.atom.o(module) 
  var __ = carbon.fibers.__(module, true) 

  __(function() {
    module.exports = o({
      _type: carbon.carbond.Service,
      port: 8888,
      verbosity: 'info',
      .
      .
      .
    })
  })

2. Using the ``-v, --verbosity`` flag at the commandline to specifity
   the verbosity level, which will set the value of the ``verbosity``
   property on your ``Service`` object. 

.. code-block:: sh 

  % node <path-to-your-app>/MyService -v info


Logging output
--------------

All output of the logging facility is directed to stderr. This can
then be piped manually or via a process manager into log files or to
implement more elaborate logging strategies.
