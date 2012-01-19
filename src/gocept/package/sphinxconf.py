# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

import datetime
import pkginfo
import sys


def set_defaults():
    _confpy = sys._getframe(1).f_locals

    _dist = pkginfo.Develop('../src/')
    project = _dist.name

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
    copyright = u'%s %s' % (_year, _dist.author)

    source_suffix = '.txt'
    master_doc = 'index'

    needs_sphinx = '1.0'
    extensions = []

    #html_theme = 'gocept' # XXX not yet implemented
    sidebars = {
        '**': ['globaltoc.html', 'searchbox.html']
    }
    pygments_style = 'sphinx'
    html_show_sourcelink = False

    for key, value in locals().items():
        if key not in _confpy:
            _confpy[key] = value
