from django import forms
from .models import Vendor_profile,TripPlan
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name')

class VendorProfileForm(forms.ModelForm):
  class Meta:
    model = Vendor_profile
    fields = ('bio', 'hood','profile_pic', 'phone_number', 'current_location','destination',)

class TripPlanForm(forms.ModelForm):
  class Meta:
    model = TripPlan
    fields = ('current_location','destination',)


class LoginForm(forms.ModelForm):
  class Meta:
    model = Vendor_profile
    fields = ('username','password',)


class SignupForm(forms.ModelForm):
  class Meta:
    model = Vendor_profile
    fields = ('username','password','profile_pic','hood','phone_number')