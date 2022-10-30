from enum import unique
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Thing(models.Model):
    REQUIRED_FIELDS = ('thing',)


    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.SmallIntegerField(unique=False, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    
    


