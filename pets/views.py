from django.shortcuts import render
from .models import Pet
from .forms import PetSearchForm
# Create your views here.


def pet_profiles(request):
    pets = Pet.objects.all()  # Fetch all pets from the database
    return render(request, 'PawsitiveAdoptionHub/templates/pets/pet_profiles.html', {'pets': pets})

# Implement other views for adoption application, pet details, etc.

def search_pets(request):
    form = PetSearchForm(request.GET)
    pets = Pet.objects.all()  # Get all pets initially

    if form.is_valid():
        species = form.cleaned_data.get('species')
        age = form.cleaned_data.get('age')

        # Create a filter dictionary for fields that are not empty
        filters = {}
        if species:
            filters['species'] = species
        if age:
            filters['age'] = age
        # Add more filters for other form fields if needed

        # Filter pets based on the filter dictionary
        pets = Pet.objects.filter(**filters)

    context = {
        'form': form,
        'pets': pets
    }
    return render(request, 'PawsitiveAdoptionHub/templates/pets/search_pet.html', context)
def home(request):
    return render(request ,"PawsitiveAdoptionHub/templates/pets/home.html")