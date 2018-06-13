from django import forms
from .models import Buyer_profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name')

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Buyer_profile
    fields = ('bio', 'location','profile_pic', 'phone_number')

class MakeForm(forms.ModelForm):

    '''
    a form that saves the buyers information when they make a an order
    '''
class Meta:
    model=User
    fields=('phone_number','Payment_method')
