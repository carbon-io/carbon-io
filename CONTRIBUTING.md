# Contributing to Carbon.io

Thank you for considering contributing to Carbon.io. We're excited to build a great framework for command line programs, microservices, and APIs. We hope a wide range of people will come together to help build Carbon.io.

Following these guidelines will help you get started contributing to Carbon.io. We love to receive new contributions! There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into Carbon.io itself.

## Your First Contribution
If you're unsure where to begin contributing to Carbon.io, feel free to [submit an issue](https://github.com/carbon-io/carbon-io/issues/new) asking for guidance. We'll be happy to help find something for you.  

A good starting point can be improving the docs. If you find anything missing or unclear, we'd love to receive input from you.

## Project Structure

Carbon.io is made out of several different repositories:

- [`carbon-io`](https://github.com/carbon-io/carbon-io): The main repository which wraps the `carbon-core` modules and `carbond`
  - [`carbond`](https://github.com/carbon-io/carbond): The server component of the Carbon.io framework
  - [`carbon-core`](https://github.com/carbon-io/carbon-core): Wrapper for the modules that make up the Carbon.io framework
    - [`atom`](https://github.com/carbon-io/atom): Dependency Injection library for creating re-usable Javascript components and command-line programs
    - [`bond`](https://github.com/carbon-io/bond): Name resolver for Carbon.io
    - [`ejson`](https://github.com/carbon-io/ejson): Utility for MongoDB Extended JSON
    - [`fibers`](https://github.com/carbon-io/fibers): Coroutines for Node.js
    - [`http-errors`](https://github.com/carbon-io/http-errors): Error classes representing HTTP error codes
    - [`leafnode`](https://github.com/carbon-io/leafnode): MongoDB driver using fibers
    - [`logging`](https://github.com/carbon-io/logging): Logger for Carbon.io
    - [`test-tube`](https://github.com/carbon-io/test-tube): Testing framework for Carbon.io

You will want to work on and submit a pull request to the repository you wish to change. If you need any help, feel free to [create an issue on `carbon-io`](https://github.com/carbon-io/carbon-io/issues/new). 

## Testing and Submitting a Pull Request

1. Create your own fork of the code
    ```
    $ git clone https://github.com/carbon-io/carbon-io
    ```
2. Do the changes in your fork
3. Run tests 
    ```
    $ npm install
    $ node test
    ```
3. Send a pull request

Working on your first Pull Request? You can learn how from this series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

## Building the docs

You can find up to date instructions on how to build the docs on the [docs README](https://github.com/carbon-io/carbon-io/blob/master/docs/README.md).

## Asking for help

Feel free to ask for help by submitting an issue. Thank you for considering contributing to Carbon.io.
