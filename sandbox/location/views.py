from django.shortcuts import render
from location.forms import PlaceForm

def home(request):
    return render(request, "location/home.html", {"form": PlaceForm()})