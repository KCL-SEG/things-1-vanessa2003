from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Thing(models.Model):
    REQUIRED_FIELDS = ('thing',)


    name = models.TextField()
    description = models.TextField()
    quantity = models.SmallIntegerField()
    
    


