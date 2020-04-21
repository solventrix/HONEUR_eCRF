"""
entrytool - Our Opal Application
"""
from opal.core import application
from opal.core import menus

from django.utils.translation import gettext_lazy as _

class Application(application.OpalApplication):
    javascripts   = [
        'js/entrytool/routes.js',
    ]

    menuitems = [
        menus.MenuItem(
            href="/#/list/", activepattern="/list/",
            icon="fa-table", display="Lists",
            index=0
        ),
        menus.MenuItem(
            href='/pathway/#/add_patient',
            display=_('Add Patient'),
            icon='fa fa-plus',
            activepattern='/pathway/#/add_patient'
        )
    ]

