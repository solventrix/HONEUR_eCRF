"""
entrytool - Our Opal Application
"""
from opal.core import application
from opal.core import menus
from entrytool.episode_categories import Default

from django.utils.translation import gettext_lazy as _


class Application(application.OpalApplication):

    javascripts   = [
        'js/entrytool/routes.js',
        "js/entrytool/controllers/lot_creator.js",
    ]

    default_episode_category=Default.display_name

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

