Carbon.io
==========

***
Tagging and publishing
----------

To make a new tag:

* git commit -am "commit message"
* git tag -a "version" -m "version"
* git push --tags origin master
* npm3 login
* npm3 publish (should work with < version 3 of npm as well) 
