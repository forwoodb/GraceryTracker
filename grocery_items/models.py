from django.db import models
from decimal import Decimal

# Create your models here.
class GroceryItem(models.Model):
    item = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    price_type = models.CharField(max_length=100, null=True, blank=True)
    servings = models.CharField(max_length=100, null=True, blank=True)
