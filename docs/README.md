# docs_carbon_io

## Installation

We use [Sphinx](http://www.sphinx-doc.org/en/stable/) to build the documentation.
 
### Dependencies

In order to use Sphinx, you will need to have [Python](https://www.python.org/downloads/) installed.

- [Sphinx](http://www.sphinx-doc.org/en/stable/) (version >= 1.3.5)
- [sphinx-autobuild](https://pypi.python.org/pypi/sphinx-autobuild) (version >= 0.5.2)
- [sphinx_rtd_theme](https://github.com/snide/sphinx_rtd_theme) (version => 0.1.9)
- [livereload](https://pypi.python.org/pypi/livereload) (version == 2.4.0)

We also recommend using [virtualenv](https://virtualenv.readthedocs.org/en/latest/index.html) to create isolated Python environments. Run the following to create and activate a new environment in your current working directory:

```sh
% [sudo] pip install virtualenv
% virtualenv ENV
% source /ENV/bin/activate
```

Consult the virtualenv [installation guide](https://virtualenv.readthedocs.org/en/latest/installation.html) for alternative methods.

To deactivate the environment:

```sh
% deactivate
```

Install the documentation dependencies:

```sh
% pip install -r requirements.txt
```

Pull in git submodules:

```sh
% git submodule update --init --recursive
```

## Run the project

You may want 'make clean' if you make edits to CSS or JS files, as Sphinx's auto-build library may not catch your changes.

```sh
% make clean html
```

```sh
% make livehtml

http://localhost:8000/
```
## Running tests

You can test the project by using ``tox``.
Simply run it in the root directory::

    tox
