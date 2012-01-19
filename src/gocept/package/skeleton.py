# Copyright (c) 2012 gocept gmbh & co. kg
# See also LICENSE.txt

from paste.script.templates import var
import datetime
import paste.script.templates
import paste.util.template


class Skeleton(paste.script.templates.Template):

    summary = (
        'Python package with buildout, conforming to conventions at gocept')

    _template_dir = 'skeleton'

    template_renderer = staticmethod(
        paste.util.template.paste_script_template_renderer)

    vars = [
    ]

    def underline_double(self, text):
        return '%s\n%s' % (text, '='*len(text))

    def pre(self, command, output_dir, vars):
        vars['namespace'], vars['package'] = vars['egg'].split('.')
        vars['year'] = datetime.date.today().year
        vars['underline_double'] = self.underline_double

    def post(self, command, output_dir, vars):
        pass
