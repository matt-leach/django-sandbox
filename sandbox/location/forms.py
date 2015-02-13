from django.forms import ModelForm
from location.models import Place

class PlaceForm(ModelForm):
    class Meta:
        model = Place
