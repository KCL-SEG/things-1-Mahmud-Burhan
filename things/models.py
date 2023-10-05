from django.db import models

class User(models.Model):
    name = models.CharField()
    description = models.CharField()
    quantity = models.IntegerField()

