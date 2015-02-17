from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'bootstrap.views.example', name='example'),
    url(r'^crispy/$', 'bootstrap.views.crispy', name='crispy'),
    )