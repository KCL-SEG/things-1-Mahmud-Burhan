from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(max_length=30)

    description = models.CharField(max_length=120)
        
    quantity = models.IntegerField()
        
