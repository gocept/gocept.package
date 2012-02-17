# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import datetime
import gocept.package
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
        file_path = os.path.join(
            self.tmpdir, 'gocept.example', *rel_path.split('/'))
        self.assertTrue(os.path.isfile(file_path))
        return open(file_path).read()


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

    @property
    def gocept_package_dev(self):
        path = gocept.package.__file__
        for _ in xrange(4):
            path = os.path.dirname(path)
        return path

    def buildout(self):
        subprocess.call([sys.executable, 'bootstrap.py'])
        return subprocess.call([
                os.path.join('bin', 'buildout'),
                'buildout:develop+=%s' % self.gocept_package_dev])

    def test_bootstrap_succeeds_using_distribute_by_default(self):
        subprocess.call([sys.executable, 'bootstrap.py'])
        bin_buildout = self.content('bin/buildout')
        self.assertIn(sys.executable, bin_buildout)
        self.assertIn('distribute-', bin_buildout)
        self.assertNotIn('setuptools-', bin_buildout)

    def test_buildout_succeeds(self):
        status = self.buildout()
        self.assertEqual(0, status)
        self.assertEqual(
            ['buildout', 'doc', 'test'], sorted(os.listdir('bin')))

    def test_tests_succeed(self):
        self.buildout()
        bin_test = os.path.join('bin', 'test')
        self.assertTrue(os.path.isfile(bin_test))
        status = subprocess.call([bin_test])
        self.assertEqual(0, status)

    def test_sphinx_docs_can_be_built(self):
        self.buildout()
        bin_doc = os.path.join('bin', 'doc')
        self.assertTrue(os.path.isfile(bin_doc))
        subprocess.call([bin_doc])
        self.assertIn('<html', self.content('build/doc/index.html'))

    def test_sphinx_api_docs_are_updated_with_every_run(self):
        self.buildout()
        bin_doc = os.path.join('bin', 'doc')
        api_txt = open(os.path.join('doc', 'api.txt'), 'w')
        api_txt.write("""\
.. autosummary::
    :toctree: ./

    gocept.example.foo
""")
        api_txt.close()
        foo_py = open(os.path.join('src', 'gocept', 'example', 'foo.py'), 'w')
        foo_py.write('"""First version of this doc string."""')
        foo_py.close()
        subprocess.call([bin_doc])
        self.assertIn('First version',
                      self.content('build/doc/gocept.example.foo.html'))
        foo_py = open(os.path.join('src', 'gocept', 'example', 'foo.py'), 'w')
        foo_py.write('"""Second version of this doc string."""')
        foo_py.close()
        subprocess.call([bin_doc])
        self.assertIn('Second version',
                      self.content('build/doc/gocept.example.foo.html'))
