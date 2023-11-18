from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='static/pet_photos/')
    medical_history = models.TextField()
    adoption_status = models.BooleanField(default=False)
    TEMPERAMENT_CHOICES = (
        ('friendly', 'Friendly'),
        ('calm', 'Calm'),
        ('playful', 'Playful'),
        # Add more temperament choices as needed
    )
    SIZE_CHOICES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        # Add more size choices as needed
    )
    SPECIES_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        # Add more species choices as needed
    )
    species = models.CharField(max_length=50, choices=SPECIES_CHOICES,null=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, null=True, blank=True)
    temperament = models.CharField(max_length=50, choices=TEMPERAMENT_CHOICES,null=True)
    # Add other fields as needed
    def __str__(self):
        return self.name