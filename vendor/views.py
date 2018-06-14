from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm, VendorProfileForm,TripPlanForm
from .models import Vendor_profile,TripPlan
from buyer.models import Buyer_profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction

# Create your views here.
def vendor(request):
  user = User.objects.get(username = request.user.username)
  profile = Vendor_profile.objects.get(user =user)
  buyer = Buyer_profile.objects.all()
  if request.method == 'POST':
    trip_form = TripPlanForm(request.POST)
    if trip_form.is_valid():
      trip_plan= TripPlan(vendor_profile = request.user.vendor_profile, current_location = request.POST['current_location'],destination = request.POST['destination'])
      trip_plan.save()
      print('success')
      return redirect(reverse('vendor:vendor'))
  else:
    trip_form = TripPlanForm()
  return render(request, 'vendor/vendor.html',{"profile": profile, "buyer": buyer, "trip_form":trip_form})

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
      return redirect(reverse('vendor:profile', kwargs = {'username': request.user.username}))
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


def buyer_profile(request,buyer_profile_id):
  user= User.objects.get(id = buyer_profile_id)
  if user:
    buyer_profile = buyer_profile.objects.get(user=user)
  return render(request,'vendor/buyer_profile.html',{"buyer_profile": buyer_profile})
