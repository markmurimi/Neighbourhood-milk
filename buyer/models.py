from django.db import models

# Create your models here.
class Buyer(models.Model):
  username = models.CharField(max_length=30)
  house_number = models.CharField(max_length = 30)
  bio = models.TextField(max_length=200)
  location = models.CharField(max_length = 50)
  phone_number =models.IntegerField()
  password = models.CharField(max_length = 40)
  profile_pic = models.ImageField(upload_to = 'Buyers')

  def __str__(self):
    return self.username

  @classmethod
  def get_buyers(cls):
    profiles = Buyer.objects.all()
    return profiles

class Order(models.Model):
  username = models.CharField(max_length=30)
  quantity = models.CharField(max_length = 30)
  house_number = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  phone_number = models.CharField(max_length=30)

  def __str__(self):
    return self.username
    
  @classmethod
  def get_orders(cls):
    orders = Order.objects.all()
    return orders