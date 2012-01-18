# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import gocept.package.doc
import gocept.testing.assertion
import os.path
import shutil
import subprocess
import sys
import tempfile
import unittest2 as unittest


class DocBuildEndtoend(unittest.TestCase, gocept.testing.assertion.Ellipsis):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.cwd = os.getcwd()
        os.chdir(self.tmpdir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tmpdir)

    def mkdir(self, path):
        os.mkdir(os.path.join(self.tmpdir, path))

    def write(self, path, contents):
        with open(os.path.join(self.tmpdir, path), 'w') as f:
            f.write(contents)

    def test_should_generate_documentation(self):
        self.write('setup.py', """\
from setuptools import setup

setup(
    name='testpackage',
    version='1.0',
    author='Author',
)
""")
        subprocess.call([sys.executable, 'setup.py', 'egg_info'])
        self.mkdir('doc')
        self.write('doc/conf.py', 'from gocept.package.sphinxconf import *')
        self.write('doc/index.txt', 'foo and bar and qux')
        gocept.package.doc.main()
        index_html = os.path.join(self.tmpdir, 'build/doc/index.html')
        self.assertTrue(os.path.isfile(index_html))
        contents = open(index_html).read()
        self.assertEllipsis('...foo and bar and qux...', contents)
