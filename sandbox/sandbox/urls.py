from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sandbox.views.home', name='home'),
    url(r'^bootstrap/', include('bootstrap.urls')),
    url(r'^location/', include('location.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^whatsget/', 'sandbox.urls.printget')
)

def printget(request):
    return HttpResponse(request.GET.items())
