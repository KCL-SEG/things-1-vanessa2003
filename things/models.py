from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Thing(models.Model):
    description = models.TextField()
    quantity = models.SmallIntegerField()
    name = models.TextField()


