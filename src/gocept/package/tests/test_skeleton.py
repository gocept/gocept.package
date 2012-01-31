# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import paste.script.command
import shutil
import tempfile
import unittest


class Skeleton(unittest.TestCase):

    def setUp(self):
        self.cwd = os.getcwd()
        self.tmpdir = tempfile.mkdtemp()
        os.chdir(self.tmpdir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tmpdir)

    def test_expand_template(self):
        paste.script.command.run(
            'create -t gocept_package gocept.example'.split())
