from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .import views

app_name = 'buyer'

urlpatterns = [
  url(r'^signup/', views.signup, name='signup'),
  url(r'^welcome/',views.welcome, name = 'welcome'),
  url(r'^accounts/', include('registration.backends.simple.urls')),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  url(r'^vendor_profile/(\d+)/$', views.vendor_profile, name='vendor_profile'),
  url(r'^bookings/(\d+)/$', views.booking_seat, name ='bookings'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
