# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import pkg_resources


def main():
    sphinx_build = pkg_resources.load_entry_point(
        'Sphinx', 'console_scripts', 'sphinx-build')
    sphinx_build(
        ['sphinx-build', '-E'] +
        [os.getcwd() + x for x in ['/doc', '/build/doc']])
