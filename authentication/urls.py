from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   
    path('/signup', views.signup),
   # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('/signin', views.signin),
    path('/signout', views.signout),
]
