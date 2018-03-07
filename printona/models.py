from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=30)
    phone_number = models.IntegerField(default=0)

class Order(models.Model):
    date_placed = models.DateTimeField('date published',auto_now=True)
    name = models.CharField( max_length=100)
    surname = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    surburb = models.CharField(max_length=100)
    city = models.CharField( max_length=100)
    postal_code = models.CharField( max_length=100)
    shipping_cost = models.DecimalField(max_digits=5, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    width = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.CharField(max_length=200)
    quality = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=5, decimal_places=2)

class OrderItem(models.Model):
    order_id = models.CharField(max_length=200)
    product_id = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    file_name = models.ImageField(upload_to="uploads")
