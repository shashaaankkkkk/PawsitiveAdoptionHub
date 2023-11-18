from django.shortcuts import render
from .models import Pet
# Create your views here.


def pet_profiles(request):
    pets = Pet.objects.all()  # Fetch all pets from the database
    return render(request, 'PawsitiveAdoptionHub/templates/pets/pet_profiles.html', {'pets': pets})

# Implement other views for adoption application, pet details, etc.
