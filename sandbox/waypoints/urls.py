from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'waypoints.views.get_waypoints', name="get_waypoints"),
    url(r'^add/$', 'waypoints.views.add_waypoint', name="add_waypoint"),
    url(r'^map/$', 'waypoints.views.home', name="view_waypoints")

)
