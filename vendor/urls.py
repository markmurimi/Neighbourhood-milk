from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

app_name = 'vendor'

urlpatterns = [
  url(r'^vendor',views.vendor, name = 'vendor'),
  url(r'^accounts/', include('registration.backends.simple.urls')),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  url(r'^buyer_profile/(\d+)/$', views.buyer_profile, name='buyer_profile'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
