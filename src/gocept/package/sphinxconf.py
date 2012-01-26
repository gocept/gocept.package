# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import datetime
import pkginfo
import pkg_resources
import sys


def set_defaults(egg=True):
    _confpy = sys._getframe(1).f_locals

    author = 'gocept'
    if egg:
        _dist = pkginfo.Develop('../src/')
        project = _dist.name
        author = _dist.author

        release = _dist.version
        version = []
        for x in release:
            try:
                version.append(str(int(x)))
            except ValueError:
                break
        version = '.'.join(version)

    _year = datetime.date.today().year
    _year_started = _confpy.get('_year_started', _year)
    if str(_year) != str(_year_started):
        _year = u'%s-%s' % (_year_started, _year)
    copyright = u'%s %s' % (_year, author)

    source_suffix = '.txt'
    master_doc = 'index'

    needs_sphinx = '1.0'
    extensions = []

    html_theme_path = [
        pkg_resources.resource_filename('gocept.package', 'themes')]
    html_theme = 'gocept'

    html_sidebars = {
        '**': ['project-links.html', 'globaltoc.html', 'searchbox.html']
    }
    html_logo = pkg_resources.resource_filename(
        'gocept.package', 'themes/gocept/static/gocept.png')
    html_favicon = pkg_resources.resource_filename(
        'gocept.package', 'themes/gocept/static/favicon.ico')
    html_show_sourcelink = False

    for key, value in locals().items():
        if key not in _confpy:
            _confpy[key] = value
