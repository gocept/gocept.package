==============
gocept.package
==============

This package is to express our conventions for Python packages.

It consists of two parts: a Python module that is used to configure Sphinx,
along with the necessary package dependencies, and a paster template that
creates the boilerplate for a Python package in the first place.

Usage
=====

To use the Sphinx configuration, add a zc.buildout section like this:

::
    [docs]
    recipe = zc.recipe.egg
    eggs = gocept.package [doc]

This installs a console script bin/doc which you can run to build your Sphinx
docs. The script assumes that the documentation source is inside a
subdirectory doc/ of your current working directory and it will put the built
documentation into build/doc/ (also relative to your working directory).

Also, there needs to exists a Sphinx configuration file at doc/conf.py:

::
    from gocept.package.sphinxconf import *

To make the paster template available, install gocept.package where paster can
find it (ignoring the doc extra). Then run paster:

::
    $ paster create --template gocept_package NAMESPACE.PROJECTNAME

The template will generate buildout.cfg and doc/conf.py files as above.
