from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=50)
    content = models.TextField()
    reporter = models.ForeignKey(User)