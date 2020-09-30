from opal.urls import urlpatterns as opatterns

from django.contrib import admin
from django.conf.urls import include, url
from entrytool import api

admin.autodiscover()

urlpatterns = [
    url(r'entrytool/v0.1/', include(api.entrytool_router.urls)),
]

urlpatterns += opatterns
