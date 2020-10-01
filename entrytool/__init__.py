"""
entrytool - Our Opal Application
"""
from opal.core import application
from opal.core import menus
from entrytool.episode_categories import Default

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Application(application.OpalApplication):

    javascripts   = [
        'js/entrytool/routes.js',
        "js/entrytool/directives.js",
        "js/entrytool/controllers/lot_creator.js",
        "js/entrytool/controllers/regimen_check.js",
    ]

    styles = [
        "css/entrytool.css"
    ]

    default_episode_category=Default.display_name

    @classmethod
    def get_menu_items(klass, user=None):
        # we import here as settings must be set before this is imported
        from django.contrib.auth.views import logout as logout_view

        menuitems = []
        if user:
            if user.is_authenticated:
                menuitems = [
                    menus.MenuItem(
                        href='/pathway/#/add_patient',
                        display=_('Add Patient'),
                        activepattern='/pathway/#/add_patient'
                    ),
                    menus.MenuItem(
                        href=reverse(logout_view), display=_('Log Out'), index=1000
                    )
                ]
                if user.is_staff:
                    menuitems.append(
                        menus.MenuItem(
                            href="/admin/", display="Admin",
                            index=999
                        )
                    )


        return menuitems
