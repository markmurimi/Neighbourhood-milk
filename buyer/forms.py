from django import forms
from .models import Buyer, Order
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Buyer
    fields = ('bio', 'location','profile_pic', 'phone_number')

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Buyer
    fields = ('username', 'password', 'phone_number', 'profile_pic', 'bio', 'location', 'house_number')

class OrderForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ('username', 'quantity', 'house_number', 'location', 'phone_number')

class LoginForm(forms.ModelForm):
  class Meta:
    model = Buyer
    fields = ('username', 'password')
