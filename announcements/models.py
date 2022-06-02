import uuid
from django.db import models
from users.models import User

GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
TYPE_CHOICES = (
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    )
STATUS = (
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    )

class FoundedPet(models.Model):
    pet_image = models.ImageField(null=True, upload_to='announcements/founded')
    title = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, default='Active')
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(max_length=750, null=True)
    city = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) + " - " + str(self.city)

    class Meta:
        ordering = ['status', '-created']

class FoundedPetComment(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    announce = models.ForeignKey(FoundedPet, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=120, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.announce) + " - " + str(self.owner)

    class Meta:
        ordering = ['created']

class AdoptPet(models.Model):
    pet_image = models.ImageField(null=True, upload_to='announcements/adopt')
    title = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, default='Active')
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(max_length=750, null=True)
    city = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) + " - " + str(self.city)

    class Meta:
        ordering = ['status', '-created']

class AdoptPetComment(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    announce = models.ForeignKey(AdoptPet, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=120, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.announce) + " - " + str(self.owner)

    class Meta:
        ordering = ['created']

class LostPet(models.Model):
    pet_image = models.ImageField(null=True, upload_to='announcements/lost')
    title = models.CharField(max_length=50, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True, default='Active')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11, null=True)
    info = models.TextField(max_length=750, null=True)
    city = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.title) + " - " + str(self.city)

    class Meta:
        ordering = ['status', '-created']

class LostPetComment(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    announce = models.ForeignKey(LostPet, null=True, on_delete=models.CASCADE)
    body = models.TextField(max_length=120, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.announce) + " - " + str(self.owner)

    class Meta:
        ordering = ['created']






