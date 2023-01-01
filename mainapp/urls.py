from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('jsonlink/',views.jsonlink,name='jsonlink'),
]