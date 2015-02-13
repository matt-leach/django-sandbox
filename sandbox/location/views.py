from django.shortcuts import render
from location.forms import PlaceForm, POIForm

def home(request):
    return render(request, "location/home.html", {"form": PlaceForm()})

def geoposition(request):
    return render(request, "location/home.html", {"form": POIForm()})