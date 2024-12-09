from django.db import models

# Create your models here.
class Stable(models.Model):
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=2)
    phone = models.CharField(max_length=10)
    clas = models.CharField(max_length=10)
