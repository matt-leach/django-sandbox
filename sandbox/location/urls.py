from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'location.views.home', name='home'),
    url(r'^geo/', 'location.views.geoposition', name='geo'),
)