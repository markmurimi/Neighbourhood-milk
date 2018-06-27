from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from . import views

app_name = 'vendor'

urlpatterns = [
  url(r'^vendor',views.vendor, name = 'vendor'),
  url(r'^signup/', views.signup, name='signup'),
  url(r'^ingia/', views.ingia, name='/ingia'),
  url(r'^profile/(?P<username>[-_\w.]+)/$', views.profile, name='profile'),
  url(r'^profile/(?P<username>[-_\w.]+)/edit/$', views.update_profile, name='edit'),
  ]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
