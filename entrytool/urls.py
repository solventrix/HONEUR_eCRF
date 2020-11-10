import os
from django.conf.urls import url
from opal.urls import urlpatterns as opatterns

from django.contrib import admin
from django.urls import path, include

from django.views.i18n import JavaScriptCatalog
from . import views

from entrytool import api

admin.autodiscover()

urlpatterns = [
    path('entrytool/v0.1/', include(api.entrytool_router.urls)),
    path('angular-locale.js', views.AngularLocale.as_view(), name="angular-locale"),
    path(
        "jsi18n/",
        JavaScriptCatalog.as_view(domain="django"),
        name="javascript-catalog",
    ),
]

urlpatterns += opatterns

if os.environ.get('OPAL_CONTEXT_PATH'):
    pattern = r'^' + os.environ.get('OPAL_CONTEXT_PATH') + '/'
    urlpatterns = [url(pattern, include(urlpatterns))]
