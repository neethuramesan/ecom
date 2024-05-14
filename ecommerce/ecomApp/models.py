
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):

    cat_name = models.CharField(max_length=100)

    def __str__(self) :
        return self.cat_name
        

class product(models.Model):
    category = models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    prod_name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'image/product/',null=True,blank = True)
    price = models.IntegerField()

class usermember(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255)
    c_num = models.CharField(max_length=12,null=True)
    profile_pic = models.ImageField(upload_to = 'image/profile/',null=True,blank = True)

class cart1(models.Model):
    product = models.ForeignKey(product,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
