from django import forms
from .models import Buyer
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Buyer
    fields = ('bio', 'location','profile_pic', 'phone_number')

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Buyer
    fields = ('username', 'profile_pic', 'phone_number','bio', 'location', 'house_number')