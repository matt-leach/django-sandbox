from django.db import models


class Waypoint(models.Model):
    name = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=10, decimal_places=5)
    long = models.DecimalField(max_digits=10, decimal_places=5)

    def __unicode__(self):
        return self.name
