"""
Override the Django Makemessages command to include database
contents in messages files
"""
import os

from django.conf import settings
from django.core.management.commands import makemessages as django_makemessages
import jinja2
import opal
from opal.core import lookuplists

FILENAME = os.path.join(settings.PROJECT_PATH, 'wow_strings.py')
TEMPLATE = os.path.join(settings.PROJECT_PATH, 'templates/wow_strings.jinja2')

REAL_OPAL = os.path.dirname(opal.__file__)
OUR_OPAL  = os.path.join(settings.PROJECT_PATH, 'opal')

class Command(django_makemessages.Command):

    def cleanup(self):
        os.remove(FILENAME)
        os.remove(OUR_OPAL)

    def create_nonsense_file(self):
        strings = []

        for lookuplist in lookuplists.lookuplists():
            for item in lookuplist.objects.all():
                strings.append(item.name)

        template = jinja2.Template(open(TEMPLATE, 'r').read())
        contents = template.render(strings=strings)
        with open(FILENAME, 'w') as fh:
            fh.write(contents)

    def symlink_opal(self):
        os.symlink(REAL_OPAL, OUR_OPAL)

    def handle(self, *a, **k):
        try:
            k['symlinks'] = True
            self.create_nonsense_file()
            self.symlink_opal()
            super(Command, self).handle(*a, **k)
        finally:
            self.cleanup()
