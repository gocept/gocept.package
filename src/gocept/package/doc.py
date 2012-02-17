# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import os
import os.path
import pkg_resources
import shutil
import sys
import tempfile


def main(argv=sys.argv):
    # We use the autosummary extension to build API docs from source code.
    # However, this extension doesn't update the generated docs if the source
    # files change. Therefore, we'd need to remove the generated stuff between
    # runs. In order to avoid the risk of accidentally deleting too much stuff
    # from the user's working copy, we work on a temporary (partial) copy of
    # the project and throw it away if the sphinx run succeeds.

    cwd = os.getcwd()
    tmpdir = tempfile.mkdtemp()
    tmpdoc = os.path.join(tmpdir, 'doc')
    shutil.copytree('doc', tmpdoc, symlinks=True)

    for name in os.listdir(cwd):
        if name.endswith('.txt'):
            shutil.copy2(name, os.path.join(tmpdir, name))

    # We also need access to the source code tree (if it still exists) since
    # our config code tries to infer some values from package info.
    src = os.path.join(cwd, 'src')
    if os.path.exists(src):
        os.symlink(src, os.path.join(tmpdir, 'src'))

    sphinx_build = pkg_resources.load_entry_point(
        'Sphinx', 'console_scripts', 'sphinx-build')
    argv = ['sphinx-build'] + argv[1:]
    argv += ['-E', tmpdoc, os.path.join(cwd, 'build', 'doc')]

    try:
        sphinx_build(argv)
    except Exception:
        print '\nFailed building docs in %s:\n\n' % tmpdoc
    else:
        shutil.rmtree(tmpdir)
