# docs_carbon_io

## Requirements

We use [Sphinx](http://www.sphinx-doc.org/en/stable/) to build the documentation. In order to use Sphinx, you will need to have [Python](https://www.python.org/downloads/) installed. 

We recommend using [virtualenv](https://virtualenv.readthedocs.org/en/latest/index.html) to create isolated Python environments and will use it in our examples below.

## Steps for setting up a local environment

Clone the repository to a directory of your choice. We'll use PROJECT_ROOT in our examples. Then change to the PROJECT_ROOT directory.

```sh
% git clone https://github.com/carbon-io/carbon-io PROJECT_ROOT
% cd PROJECT_ROOT
```

Create and activate a new Python environment.

```sh
% virtualenv env
% source PROJECT_ROOT/env/bin/activate
```

Note: In the example above, the virtualenv is named 'env' and resides in the project's root directory. It is possible to have this environment reside elsewhere - that is left to the developer's discretion.

Carbon.io is built on several core components. To include the documentation for these components, include the submodules.

```sh
% git submodule update --init --recursive
```

Install the documentation dependencies.

```sh
% pip install -r PROJECT_ROOT/docs/requirements.txt
```

## Run the project

```sh
% make clean && make livehtml

http://localhost:8000/
```

## Example: Making changes to a submodule's documentation and pushing the changes live

This example demonstrates how to update and push the documentation for the Atom project.

From the PROJECT_ROOT, change to the `atom/docs` directory.

```sh
% cd PROJECT_ROOT/docs/packages/carbon-core/docs/packages/atom/docs
```

Checkout the master branch. This will configure Atom to use the remote master branch HEAD reference and allow `push` and `pull` commands to work.

```sh
% git checkout master
```

Make your changes to the documentation and build the docs to review them locally. You should build the docs from the Atom `docs` folder.

```sh
% pwd
PROJECT_ROOT/docs/packages/carbon-core/docs/packages/atom/docs

% make clean && make livehtml

http://localhost:8000
```

Once the changes are finalized, open the Atom `package.json` file and bump the version number. Commit the changes, create a new tag, and push to master. **Note: the tag and tag message must match and use the convention "vMajor.Minor.Patch".**

```sh
% git commit -am "commit message"
% git tag -a "v<tag>" -m "v<tag>"
% git push --tags origin master
```

Now that the changes have been pushed, reset the submodule pointers from the carbon-io root directory. This is required for the [documentation update script](https://github.com/carbon-io/carbon-io/blob/master/.git-cmds/git-update-docs) to work.

```sh
% cd PROJECT_ROOT
% git submodule update --init --recursive
```

Run the update script. The script will compare each local submodule's version to the remote. In this case, the new Atom tag will be found. If the new tag version satisfies the parent module (Carbon Core) dependency specification, the new tag version will be pulled in locally. The script will then modify the Carbon Core `package.json` version, tag and commit the package, and push the new tag to master. The script is recursive and will continue until the top-level carbon-io package is updated.

```sh
% cd PROJECT_ROOT
% git pull
% cd .git-cmds
% ./git-update-docs -v
 
When prompted, select 'y' to commit the changes made by the script for each parent submodule.
```

## Example: Making changes to a submodule's documentation and creating a pull request

This example will perform the same modifications as above using the Atom project. However, we will instead create our changes in a branch and create a pull request.

From the PROJECT_ROOT, change to the `atom/docs` directory and checkout the master branch.

```sh
% cd PROJECT_ROOT/docs/packages/carbon-core/docs/packages/atom/docs
% git checkout master
```

Checkout your development branch using the -b option. Checking out a separate branch will allow you to create a pull request to master.

```sh
% git checkout -b "YOUR_DEV_BRANCH_NAME"
```

Make your changes to the documentation and build the docs to review them locally.

```sh
% make clean && make livehtml

http://localhost:8000
```

Commit your changes WITHOUT tagging and push your development branch.

```sh
% git commit -am "commit message"
% git push origin YOUR_DEV_BRANCH_NAME
```

Go to the Atom GitHub repository and [create a pull request](https://github.com/carbon-io/atom/compare) to merge your changes into the master branch. When your changes are approved a collaborator on the repository will merge your changes and update the submodule pointer.

## Running tests

You can test the project by using ``tox``.
Simply run it in the root directory::

    tox
