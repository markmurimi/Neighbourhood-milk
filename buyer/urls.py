from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

app_name = 'buyer'

urlpatterns = [
  url(r'^$',views.buyer, name = 'buyer'),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  url(r'^vendor_profile/(\d+)/$', views.vendor_profile, name='vendor_profile'),
  url(r'^bookings/(\d+)/$', views.booking_seat, name ='bookings'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
