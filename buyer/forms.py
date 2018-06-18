from django import forms
from .models import Buyer, Order
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Buyer
    fields = ('bio', 'location','profile_pic', 'phone_number')

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Order
    fields = ('username', 'quantity', 'phone_number', 'location', 'house_number')
