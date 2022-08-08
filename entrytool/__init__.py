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
        "js/entrytool/services/data_upload_loader.js",
        "js/entrytool/services/entrytool_record_editor.js",
        "js/entrytool/controllers/lot_manager.js",
        "js/entrytool/controllers/delete_lot.js",
        "js/entrytool/controllers/patient_validator.js",
        "js/entrytool/controllers/data_uploader.js",
        "js/entrytool/controllers/honeur_patient_detail_ctrl.js",
        "js/entrytool/moment_lang.js",
    ]

    styles = [
        "css/entrytool.css"
    ]

    default_episode_category = episode_categories.Default.display_name

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
                    ),
                    menus.MenuItem(
                        href='/#/data_upload',
                        display=_('Data Upload'),
                        activepattern='/#/data_upload'
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
