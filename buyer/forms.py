from django import forms
from .models import Buyer_profile
from django.contrib.auth.models import User

class BuyerForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Buyer_profile
    fields = ('bio', 'location','profile_pic', 'phone_number')

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Buyer_profile
    fields = ('username', 'profile_pic', 'phone_number', 'house_number')