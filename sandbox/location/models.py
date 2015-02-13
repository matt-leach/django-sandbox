from django.db import models

from location_field.models.plain import PlainLocationField


class Place(models.Model):
    name = models.CharField(max_length=255)
    plain_location = PlainLocationField(based_fields=[name], zoom=10)

    def __unicode__(self):
        return self.name