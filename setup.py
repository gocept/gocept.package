# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

"""gocept Python package conventions
"""

from setuptools import setup, find_packages
import glob
import os.path


install_requires = [
    'PasteScript',
    'distribute',
    'pkginfo',
    ]

extras_require = {
    'doc': [
        'Sphinx>=1.0',
        ],
    'test': [
        'gocept.testing',
        'unittest2',
        ],
    }

entry_points = {
    'console_scripts': [
        'doc=gocept.package.doc:main',
        ],
    'paste.paster_create_template': [
        'gocept_package = gocept.package.skeleton:Skeleton'
        ],
    }

classifiers = """\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 2 :: Only
"""[:-1].split('\n')


project_path = lambda *names: os.path.join(os.path.dirname(__file__), *names)

longdesc = '\n\n'.join((open(project_path('README.txt')).read(),
                        open(project_path('HACKING.txt')).read(),
                        open(project_path('CHANGES.txt')).read()))

data_files = [("", glob.glob(project_path("*.txt")))]


setup(name='gocept.package',
      version='1.0.dev0',
      description=__doc__.strip(),
      long_description=longdesc,
      author='Thomas Lotze <tl at gocept dot com> and Wolfgang Schnerring <ws at gocept dot com>',
      author_email="mail@gocept.com",
      url="https://projects.gocept.com/projects/gocept-package/",
      license="ZPL 2.1",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      data_files=data_files,
      zip_safe=False,
      namespace_packages=['gocept'],
      install_requires=install_requires,
      extras_require=extras_require,
      entry_points=entry_points,
      classifiers=classifiers,
      )
