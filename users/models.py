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
    full_name = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    tckn = models.CharField(max_length=11, null=True)
    phone = models.CharField(max_length=11, null=True)
    birthDate = models.DateField(null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.jpg")
    created = models.DateTimeField(auto_now_add=True)

    # business
    business_name = models.CharField(max_length=200, blank=True, null=True)
    tax_id = models.CharField(max_length=11, null=True, unique=True)
    # phone
    information = models.TextField(max_length=500, blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    logo = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/store-default.png")
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE, null=True)

    def __str__(self):
        return str(self.username) + '-' + str(self.user_type)


# class PetLover(models.Model):
#     GENDER_CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # username = models.CharField(max_length=200, blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     location = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=200, blank=True, null=True)
#     tckn = models.CharField(max_length=11, null=True, unique=True)
#     phone = models.CharField(max_length=11, null=True, unique=True)
#     birthDate = models.DateField(null=True)
#     gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
#     user_type = models.CharField(max_length=20, default="pet_lover", editable=False)
#     profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.jpg")
#     created = models.DateTimeField(auto_now_add=True)
#     petlover_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#
#
#
#     def __str__(self):
#         return str(self.full_name)


# class Pet(models.Model):
#     GENDER_CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#     )
#     TYPE_CHOICES = (
#         ('Dog', 'Dog'),
#         ('Cat', 'Cat'),
#     )
#     owner = models.ForeignKey(PetLover, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, blank=True, null=True)
#     race = models.CharField(max_length=200, blank=True, null=True)
#     height = models.CharField(max_length=200, blank=True, null=True)
#     weight = models.CharField(max_length=200, blank=True, null=True)
#     birthDate = models.DateField(null=True)
#     gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
#     pet_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="petcircle.jpg")
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#
#     def __str__(self):
#         return str(self.name) + " - " + str(self.owner)


# class Business(models.Model):
#     BUSINESS_TYPE = (
#         ('Pet Shop', 'Pet Shop'),
#         ('Pet Stylists', 'Pet Stylists'),
#         ('Pet Hotel', 'Pet Stylists'),
#         ('Veterinary', 'Veterinary'),
#         ('Other', 'Other'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     # username = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=200, blank=True, null=True, unique=True)
#     business_name = models.CharField(max_length=200, blank=True, null=True)
#     tax_id = models.CharField(max_length=11, null=True, unique=True)
#     phone = models.CharField(max_length=11, null=True, unique=True)
#     information = models.TextField(max_length=500, blank=True, null=True)
#     address = models.TextField(max_length=500, blank=True, null=True)
#     logo = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/store-default.png")
#     user_type = models.CharField(max_length=20, default="business", editable=False)
#     business_type = models.CharField(max_length=20, choices=BUSINESS_TYPE, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     business_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
#
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return str(self.business_name)

# class Admin(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     username = models.CharField(max_length=200, blank=True, null=True)
#     email = models.EmailField(max_length=200, blank=True, null=True)
#     full_name = models.CharField(max_length=200, blank=True, null=True)
#     profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.jpg")
#     user_type = models.CharField(max_length=20, default="admin", editable=False)
#     created = models.DateTimeField(auto_now_add=True)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#
#     def __str__(self):
#         return str(self.full_name)


