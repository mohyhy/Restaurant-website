from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    choices= [
        ('Vegetables','Vegetables'),
        ('Fruits','Fruits'),
        ('Juice','Juice'),
        ('Dried','Dried'),
    ]
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount  = models.FloatField(blank=True,null=True,default=0)
    image = models.ImageField() 
    category = models.CharField(choices=choices,max_length=50)
    description = models.TextField()

    
    def __str__(self):
        return self.name
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    locality = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    zipcode = models.IntegerField(blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    addrees1 = models.TextField(max_length=250,default='such as: Salah_aldeen- in nuserate',blank=True,null=True)
    addrees2 = models.TextField(max_length=250,blank=True,null=True)
    
    def __str__(self):
        return str(self.user.username)

