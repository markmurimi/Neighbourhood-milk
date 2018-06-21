from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.validators import RegexValidator
from buyer.models import Buyer


# Create your models here.
class Vendor_profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    bio = models.TextField(max_length=200, blank =True)
    hood = models.CharField(max_length = 50, blank =True)
    phone_number =models.IntegerField(blank = True, null = True)
    profile_pic = models.ImageField(upload_to = 'profile_pic/', blank=True, null= True)
    current_location = models.CharField(max_length = 10)
    destination = models.CharField(max_length = 30, blank = True, null = True)
    Free_space = models.PositiveIntegerField(default =0)

class TripPlan(models.Model):
    Vendor_profile = models.ForeignKey(Vendor_profile,on_delete=models.CASCADE )
    current_location = models.CharField(max_length = 30)
    destination = models.CharField(max_length = 30)


