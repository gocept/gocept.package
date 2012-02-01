# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import pkg_resources
import sys


def main(argv=sys.argv):
    sphinx_build = pkg_resources.load_entry_point(
        'Sphinx', 'console_scripts', 'sphinx-build')
    argv = ['sphinx-build'] + argv[1:]
    if len(argv) == 1:
        argv += ['-E'] + [os.getcwd() + x for x in ['/doc', '/build/doc']]
    sphinx_build(argv)
