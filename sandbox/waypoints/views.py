import json

from django.http import HttpResponse
from django.shortcuts import render

from waypoints.models import Waypoint


def get_waypoints(request):
    # If query parameters don't exist just use max/min long and lat values
    top = request.GET.get("top", 90)
    bottom = request.GET.get("bottom", -90)
    left = request.GET.get("left", -180)
    right = request.GET.get("right", 180)

    points = Waypoint.objects.filter(lat__lt=top, lat__gt=bottom, long__gt=left, long__lt=right)

    points = [{"lat": float(p.lat), "long": float(p.long), "name": p.name} for p in points]

    json_points = json.dumps(points)
    return HttpResponse(json_points, content_type="json")


def add_waypoint(request):

    if request.method == "POST":
        lat = float(request.POST["lat"])
        long = float(request.POST["long"])
        name = request.POST["name"]

        wp = Waypoint.objects.create(name=name, long=long, lat=lat)
        return HttpResponse(content_type="json")


def home(request):
    return render(request, "waypoints/home.html", {})
