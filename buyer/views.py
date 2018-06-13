from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm
from .models import Buyer_profile
from vendor.models import Vendor_profile,TripPlan,Booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

"""import africastalking
africastalking.initialize(username='sandbox',api_key='03024a821413da2f2db06da882a010378b589e48e0a80de0456c5d0e3fbb9923')
sms = africastalking.SMS
res = sms.send(message='hello', recipients=['+254726830125'])
"""
# Create your views here.
def buyer(request):
  user = User.objects.get(username = request.user.username)
  profile = buyer_profile.objects.get(user =user)
  vendor = Vendor_profile.objects.all()
  return render(request, 'buyer/buyer.html', {"profile": profile, "vendor":vendor})


def update_profile(request,username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance = request.user)
    profile_form = ProfileForm(request.POST, instance =request.user.buyer_profile, files = request.FILES)
    if user_form.is_valid() and profile_form.is_valid():
      print('master')
      user_form.save()
      profile_form.save()
      messages.success(request, ('Your profile was successfully updated!'))
      return redirect(reverse('buyer:profile', kwargs = {'username': request.user.username}))
    else:
      messages.error(request, ('Please correct the error below.'))

  else:
    user_form = UserForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.buyer_profile)
  return render(request, 'buyer/profiles/profile_form.html', {"user_form":user_form, "profile_form":profile_form})

@login_required
def profile(request, username):
  user = User.objects.get(username =username)
  if not user:
    return redirect('buyer')
  profiles = Buyer_profile.objects.get(user =user)

  title = f"{user.username}"

  return render(request, 'buyer/profiles/profile.html', {"title":title, "user":user, "profiles": profiles})


#Buyer sees a particular vendor's profile
def vendor_profile(request,vendor_profile_id,trip_plan_id):
  user= User.objects.get(id = vendor_profile_id)
  if user:
    vendor_profile = Vendor_profile.objects.get(user=user)
    trip_plan = TripPlan.objects.get(id = trip_plan_id)
    existing_bookings = Booking.objects.filter(trip_plan =trip_plan.id)
    if len(existing_bookings) < trip_plan.vendor_profile.car_capacity:
      seats_left = trip_plan.vendor_profile.car_capacity - len(existing_bookings)
      return render(request,'buyer/vendor_profile.html',{'vendor_profile': vendor_profile,"seats_left":seats_left,"trip_plan":trip_plan})
    elif len(existing_bookings) == trip_plan.vendor_profile.car_capacity:
      message = "this ride is fully booked"
      return render(request,'buyer/vendor_profile.html',{'vendor_profile': vendor_profile,"message":message})

def booking_seat(request, vendor_profile_id):
  current_user = request.user

  buyer_profile = Buyer_profile.objects.get(user= current_user)

  found_profile = Vendor_profile.objects.get(id = vendor_profile_id)

  trip_plan = TripPlan.objects.get(vendor_profile = found_profile)

  existing_bookings = Booking.objects.filter(trip_plan=trip_plan)

  if len(existing_bookings) < trip_plan.vendor_profile.car_capacity:
    new_booking = Booking(buyer_profile= buyer_profile, trip_plan = trip_plan)

    new_booking.save()

    print(new_booking)

  elif len(existing_bookings) == trip_plan.vendor_profile.car_capacity:
    return redirect(reverse('buyer:vendor_profile', kwargs={'vendor_profile_id':Vendor_profile.user.id}))
