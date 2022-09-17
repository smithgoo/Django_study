from django.db import models

# Create your models here.
class user(models.Model):
    phone = models.CharField(max_length=10)
    pwd = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    sex = models.IntegerField(default=0) #0未知 1男 2女
    tips = models.CharField(max_length=120)
    coins = models.IntegerField(default=0)
    avator = models.CharField(max_length=300)