# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

from setuptools import setup, find_packages


setup(name='gocept.package',
      version='1.0dev',
      description="gocept Python package conventions",
    long_description=(
        open('README.txt').read()
        + '\n\n'
        + open('CHANGES.txt').read()),
      author="Thomas Lotze <tl at gocept dot com> and Wolfgang Schnerring <ws at gocept dot com>",
      author_email="mail@gocept.com",
      url="http://gocept.com/",
      license="ZPL",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      namespace_packages=['gocept'],
      install_requires=[
        'PasteScript',
        'distribute',
        'pkginfo',
      ],
      extras_require=dict(
        doc=[
            'Sphinx',
        ],
        test=[
            'gocept.testing',
            'unittest2',
        ],
      ),
      entry_points={
        'console_scripts': [
            'doc=gocept.package.doc:main',
            ],
        'paste.paster_create_template': [
            'gocept_package = gocept.package.skeleton:Skeleton'
            ],
        },
      )
