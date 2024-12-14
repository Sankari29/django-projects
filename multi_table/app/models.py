from django.db import models
from django.core.exceptions import ValidationError
from .validations import *

class Customer(models.Model):
    first_name = models.CharField(max_length=50,validators=[v_name])
    last_name = models.CharField(max_length=50,validators=[v_name])
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,unique=True,validators=[v_phone])
    address = models.TextField(validators=[v_name])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100,validators=[v_name])
    description = models.TextField(validators=[v_desc])
    price = models.DecimalField(max_digits=10, decimal_places=2 ,validators=[validate_price])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
    def clean(self):
        if self.name==self.description:
             raise ValidationError('name and description should not be same')

