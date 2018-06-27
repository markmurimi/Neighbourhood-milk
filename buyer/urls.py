from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from .import views

app_name = 'buyer'

urlpatterns = [
  url(r'^signup/', views.signup, name='Signup/'),
  url(r'^ingia/', views.ingia, name='ingia/'),
  url(r'^order/', views.order, name='order/'),
  url(r'^payment/', views.payment, name='payment'),
  url(r'^message/', views.message, name='message'),
  url(r'^welcome/',views.welcome, name = 'welcome'),
]
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
