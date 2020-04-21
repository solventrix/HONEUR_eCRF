from opal.urls import urlpatterns as opatterns

from django.contrib import admin

from . import views

from django.conf.urls import include, url

admin.autodiscover()

urlpatterns = []

urlpatterns += opatterns
