"""
URL configuration for PawsitiveAdoptionHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pets.views import pet_profiles,search_pets ,home

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pet-profiles/', pet_profiles, name='pet_profiles'),
    path('search/', search_pets, name='search_pets'),
    path("",home),
]
