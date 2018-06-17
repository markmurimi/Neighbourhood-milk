from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
# from drivers.models import Driver_profile


# Create your models here.
class Buyer_profile(models.Model):
  username = models.CharField(max_length=30)
  house_number = models.CharField(max_length = 30)
  bio = models.TextField(max_length=200, blank =True)
  location = models.CharField(max_length = 50, blank =True)
  phone_number =models.IntegerField(blank = True, null = True)
  profile_pic = models.ImageField(upload_to = 'profile_pic/', blank=True, null= True)

  def __str__(self):
    return self.username

  @classmethod
  def get_profiles(cls):
    profiles = Buyer_profile.objects.all()
    return profiles
