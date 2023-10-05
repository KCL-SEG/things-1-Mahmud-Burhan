from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField()

    description = models.CharField()
        
    quantity = models.IntegerField()
        
