"""
Override the Django Makemessages command to include database
contents in messages files
"""
import os

from django.conf import settings
from django.core.management.commands import makemessages as django_makemessages
import jinja2
from opal.core import lookuplists

FILENAME = os.path.join(settings.PROJECT_PATH, 'wow_strings.py')
TEMPLATE = os.path.join(settings.PROJECT_PATH, 'templates/wow_strings.jinja2')

class Command(django_makemessages.Command):

    def cleanup(self):
        os.remove(FILENAME)

    def create_nonsense_file(self):
        strings = []

        for lookuplist in lookuplists.lookuplists():
            for item in lookuplist.objects.all():
                strings.append(item.name)

        template = jinja2.Template(open(TEMPLATE, 'r').read())
        contents = template.render(strings=strings)
        with open(FILENAME, 'w') as fh:
            fh.write(contents)

    def handle(self, *a, **k):
        try:
            self.create_nonsense_file()
            super(Command, self).handle(*a, **k)
        finally:
            self.cleanup()
