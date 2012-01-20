# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import pkg_resources
import sys


def main(argv=sys.argv):
    if not argv:
        argv = ['-E']
    sphinx_build = pkg_resources.load_entry_point(
        'Sphinx', 'console_scripts', 'sphinx-build')
    sphinx_build(
        ['sphinx-build'] + argv +
        [os.getcwd() + x for x in ['/doc', '/build/doc']])
