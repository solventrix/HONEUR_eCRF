from opal.urls import urlpatterns as opatterns

from django.contrib import admin
from django.urls import path, include

from django.views.i18n import JavaScriptCatalog
from . import views

from entrytool import api, views

admin.autodiscover()

urlpatterns = [
    path('entrytool/v0.1/', include(api.entrytool_router.urls)),
    path('angular-locale.js', views.AngularLocale.as_view(), name="angular-locale"),
    path(
        'validation_rules.js',
        views.ValidationRules.as_view(),
        name="validation-rules"
    ),
    path(
        "jsi18n/",
        JavaScriptCatalog.as_view(domain="django"),
        name="javascript-catalog",
    ),
    path('orphaned_records/', views.OrphanedRecords.as_view())
]

urlpatterns += opatterns
