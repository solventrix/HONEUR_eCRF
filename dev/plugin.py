"""
Plugin definition for the dev Opal plugin
"""
from opal.core import plugins

from dev.urls import urlpatterns

class DevPlugin(plugins.OpalPlugin):
    """
    Main entrypoint to expose this plugin to our Opal application.
    """
    urls = urlpatterns
    javascripts = {
        # Add your javascripts here!
        'opal.dev': [
            # 'js/dev/app.js',
            # 'js/dev/controllers/larry.js',
            # 'js/dev/services/larry.js',
        ]
    }

    def list_schemas(self):
        """
        Return any patient list schemas that our plugin may define.
        """
        return {}

    def roles(self, user):
        """
        Given a (Django) USER object, return any extra roles defined
        by our plugin.
        """
        return {}