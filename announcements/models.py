import uuid
from django.db import models


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    )

class FoundedPet(models.Model):
    pet_image = models.ImageField(null=True, upload_to='announcements/founded')
    title = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(max_length=750, null=True)
    address = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

class AdoptPet(models.Model):
    pet_image = models.ImageField(null=True, upload_to='announcements/adopt')
    title = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(max_length=750, null=True)
    address = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

class LostPet(models.Model):
    pet_image = models.ImageField(null=True, upload_to='announcements/lost')
    title = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(max_length=750, null=True)
    address = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)






