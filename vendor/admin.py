from django.contrib import admin
from vendor.models import  TripPlan, Booking, Vendor_profile

# Register your models here.
admin.site.register(Vendor_profile)
admin.site.register(TripPlan)
admin.site.register(Booking)