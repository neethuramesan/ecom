from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=255)

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    productname = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/')

class Customer(models.Model):
    address = models.CharField(max_length=255)
    contactnumber = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')