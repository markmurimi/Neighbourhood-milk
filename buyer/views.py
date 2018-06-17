from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm,ProfileForm, SignUpForm
from .models import Buyer_profile
from vendor.models import Vendor_profile,TripPlan,Booking
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.
def buyer(request):
  user = User.objects.get(username = request.user.username)
  profile = Buyer_profile.objects.get(user =user)
  vendor = Vendor_profile.objects.all()
  return render(request, 'buyer/buyer.html', {"profile": profile, "vendor":vendor})

def update_profile(request,username):
  user = User.objects.get(username = username)
  if request.method == 'POST':
    user_form = BuyerForm(request.POST, instance = request.user)
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
    buyer_form = BuyerForm(instance = request.user)
    profile_form = ProfileForm(instance = request.user.buyer_profile)
  return render(request, 'buyer/profiles/profile_form.html', {"buyer_form":user_form, "profile_form":profile_form})

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

def signup(request):
    '''
    View function to display a form for creating a post to a logged in authenticated user
    '''
    current_user = request.user

    if request.method == 'POST':

        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid:
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect(buyer)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {"form": form})
