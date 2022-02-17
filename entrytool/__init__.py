"""
entrytool - Our Opal Application
"""
from opal.core import application
from opal.core import menus
from plugins.conditions.cll.episode_categories import CLLBase

from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Application(application.OpalApplication):
    javascripts   = [
        'js/entrytool/routes.js',
        "js/entrytool/directives.js",
        'js/entrytool/filters.js',
        "js/entrytool/controllers/lot_manager.js",
        "js/entrytool/controllers/delete_lot.js",
        "js/entrytool/controllers/patient_validator.js",
        "js/entrytool/moment_lang.js",
    ]

    styles = [
        "css/entrytool.css"
    ]

    default_episode_category=CLLBase.display_name

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
                            href="/admin/", display=_("Admin"),
                            index=999
                        )
                    )


        return menuitems
