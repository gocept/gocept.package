# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import datetime
import gocept.package.doc
import os
import os.path
import paste.script.command
import shutil
import subprocess
import sys
import tempfile
import unittest


class SkeletonSetUp(unittest.TestCase):

    def setUp(self):
        self.cwd = os.getcwd()
        self.tmpdir = tempfile.mkdtemp()
        os.chdir(self.tmpdir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tmpdir)

    def expand_template(self):
        try:
            paste.script.command.run(
                'create -t gocept_package gocept.example'.split() + [
                    'description="An example package." ',
                    'keywords="example package"',
                    ])
        except SystemExit:
            pass

    def content(self, rel_path):
        return open(os.path.join(
                self.tmpdir, 'gocept.example', *rel_path.split('/'))).read()


class Skeleton(SkeletonSetUp):

    def test_expanding_template_creates_files(self):
        self.expand_template()
        self.assertEqual(
            '', self.content('src/gocept/example/tests/__init__.py'))
        self.assertIn(
            str(datetime.date.today().year), self.content('COPYRIGHT.txt'))

    def test_hg_init_has_been_run(self):
        self.expand_template()
        self.assertTrue(os.path.isdir(os.path.join('gocept.example', '.hg')))

    def test_setup_py_is_functional(self):
        # paster detects setup.py and creates egg-info from it
        self.expand_template()
        self.assertIn('Name: gocept.example\n',
                      self.content('src/gocept.example.egg-info/PKG-INFO'))

    def test_sphinx_docs_can_be_built(self):
        self.expand_template()
        os.chdir('gocept.example')
        gocept.package.doc.main(['doc'])
        self.assertIn('<html', self.content('build/doc/index.html'))


class Buildout(SkeletonSetUp):

    level = 2

    def setUp(self):
        super(Buildout, self).setUp()
        self.expand_template()
        os.chdir('gocept.example')

    def test_bootstrap_succeeds_using_distribute_by_default(self):
        subprocess.call([sys.executable, 'bootstrap.py'])
        bin_buildout = self.content('bin/buildout')
        self.assertIn(sys.executable, bin_buildout)
        self.assertIn('distribute-', bin_buildout)
        self.assertNotIn('setuptools-', bin_buildout)
