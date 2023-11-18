from django import forms

class PetSearchForm(forms.Form):
    SPECIES_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        # Add other species choices
    )
    
    species = forms.ChoiceField(choices=SPECIES_CHOICES, required=False)
    age = forms.IntegerField(min_value=0, required=False)
    size = forms.CharField(max_length=20, required=False)
    temperament = forms.CharField(max_length=50, required=False)
    # Add more fields for other criteria
