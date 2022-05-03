import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    BUSINESS_TYPE = (
        ('Pet Shop', 'Pet Shop'),
        ('Pet Stylists', 'Pet Stylists'),
        ('Pet Hotel', 'Pet Stylists'),
        ('Veterinary', 'Veterinary'),
        ('Other', 'Other'),
    )
    email = models.EmailField(null=True, unique=True)
    user_type = models.CharField(max_length=20, null=True, editable=False)
    user_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    # petlover
    full_name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    tckn = models.CharField(max_length=11, null=True)
    phone = models.CharField(max_length=11, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.jpg")
    created = models.DateTimeField(auto_now_add=True)

    # business
    business_name = models.CharField(max_length=200, null=True)
    tax_id = models.CharField(max_length=11, null=True, unique=True)
    # phone
    information = models.TextField(max_length=500, null=True)
    address = models.TextField(max_length=500, null=True)
    logo = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/store-default.png")
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE, null=True)

    def __str__(self):
        return str(self.username) + '-' + str(self.user_type)


class Pet(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    )
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    race = models.CharField(max_length=200, blank=True, null=True)
    weight = models.CharField(max_length=200, blank=True, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    pet_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="petcircle.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name) + " - " + str(self.owner)


