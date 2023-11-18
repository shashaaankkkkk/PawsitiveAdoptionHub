from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='pet_photos/')
    medical_history = models.TextField()
    adoption_status = models.BooleanField(default=False)
    # Add other fields as needed
