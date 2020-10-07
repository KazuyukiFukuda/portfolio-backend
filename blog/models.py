from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    person_name = models.TextField()
    person_age = models.IntegerField()