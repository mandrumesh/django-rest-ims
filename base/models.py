from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length = 300, unique = True)
    password = models.CharField(max_length = 300)
    email = models.EmailField()
    image = models.FileField()
    address = models.CharField(max_length = 300)
    contact = models.CharField(max_length = 300)

class Product(models.Model):
    name = models.CharField(max_length = 300)
    image = models.FileField()
    description = models.TextField()
    category = models.ForeignKey('ProductType', on_delete = models.SET_NULL, null = True)
    stock = models.IntegerField()
    department = models.ManyToManyField('Department', null = True, blank = True)

class ProductType(models.Model):
    name = models.CharField(max_length = 300)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    vendor = models.ForeignKey('Vendor', on_delete = models.SET_NULL, null = True)

class Sell(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length = 300)

class Department(models.Model):
    name = models.CharField(max_length = 300)
    floor = models.CharField(max_length = 300)

class Vendor(models.Model):
    name = models.CharField(max_length = 300)
    email = models.EmailField()
    address = models.CharField(max_length = 300)
    contact = models.CharField(max_length = 300)