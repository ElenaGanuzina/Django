import math

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now=True)


class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    add_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='image/', null=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    order_date = models.DateField(auto_now=True)





