from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, VendorProfileForm,TripPlanForm, LoginForm, SignupForm
from .models import Vendor_profile,TripPlan
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from buyer.models import Order

# Create your views here.
def vendor(request):
  orders = Order.get_orders()
  return render(request, 'vendor/vendor.html', {'orders':orders})

@transaction.atomic
def update_profile(request,username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = VendorProfileForm(request.POST, instance =request.user.vendor_profile, files = request.FILES)
    if profile_form.is_valid() and user_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('vendors:profile', kwargs = {'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))

  else:
    user_form = UserForm(instance = request.user)
    profile_form = VendorProfileForm(instance = request.user.vendor_profile)
  return render(request, 'vendor/profiles/profile_form.html', {"user_form":user_form, "profile_form":profile_form})

@login_required(login_url='/accounts/login')
def profile(request, username):
  user = User.objects.get(username =username)
  if not user:
    return redirect('vendor')
  profile = Vendor_profile.objects.get(user =user)
  print(profile.profile_pic)

  title = f"{user.username}"

  return render(request, 'vendor/profiles/profile.html', {"title":title, "user":user, "profile": profile})

def ingia(request):
    '''
    View function to display a login form
    '''
    current_user = request.user

    if request.method == 'POST':

        form = LoginForm(request.POST, request.FILES)

        if form.is_valid:
            return redirect('/vendor/vendor')
    else:
        form = LoginForm()
    return render(request, 'ingia.html', {"form": form})

def signup(request):
    '''
    View function to display a signup form
    '''
    current_user = request.user

    if request.method == 'POST':

        form = SignupForm(request.POST, request.FILES)

        if form.is_valid:
            form.save()
            post.user = current_user
            post.save()
            return redirect(message)
    else:
        form = SignupForm()
    return render(request, 'register.html', {"form": form})