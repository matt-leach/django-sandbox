from django.forms import ModelForm
from location.models import Place, PointOfInterest


class PlaceForm(ModelForm):
    class Meta:
        model = Place


class POIForm(ModelForm):
    class Meta:
        model = PointOfInterest