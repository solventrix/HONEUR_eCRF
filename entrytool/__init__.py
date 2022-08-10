"""
entrytool - Our Opal Application
"""
from opal.core import application
from opal.core import menus
from entrytool import episode_categories

from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Application(application.OpalApplication):
    javascripts   = [
        'js/entrytool/routes.js',
        "js/entrytool/directives.js",
        'js/entrytool/filters.js',
        "js/entrytool/services/entrytool_helper.js",
        "js/entrytool/services/validate_patient.js",
        "js/entrytool/services/validate_field.js",
        "js/entrytool/services/entrytool_record_editor.js",
        "js/entrytool/controllers/lot_manager.js",
        "js/entrytool/controllers/delete_lot.js",
        "js/entrytool/controllers/patient_validator.js",
        "js/entrytool/controllers/honeur_patient_detail_ctrl.js",
        "js/entrytool/moment_lang.js",
    ]

    styles = [
        "css/entrytool.css"
    ]

    default_episode_category = episode_categories.Default.display_name

    @classmethod
    def get_menu_items(klass, user=None):
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
                        href=reverse("logout"), display=_('Log Out'), index=1000
                    ),
                ]
                if user.is_staff:
                    menuitems.append(
                        menus.MenuItem(
                            href="/admin/", display=_("Admin"),
                            index=999
                        )
                    )


        return menuitems
