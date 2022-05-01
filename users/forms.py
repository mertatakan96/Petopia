from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Business, PetLover, Pet
from datetime import datetime

BUSINESS_TYPE = (
    ('Pet Shop', 'Pet Shop'),
    ('Pet Stylists', 'Pet Stylists'),
    ('Pet Hotel', 'Pet Stylists'),
    ('Veterinary', 'Veterinary'),
    ('Other', 'Other'),
)


class BusinessUserCreationForm(UserCreationForm):
    class Meta:
        model = Business
        fields = ['email', 'password1', 'password2', 'business_name',
                  'business_type', 'tax_id', 'phone', 'address', 'information']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'unicorn'}),
            'password1': forms.PasswordInput(attrs={'class': 'unicorn'}),
            'password2': forms.PasswordInput(attrs={'class': 'unicorn'}),
            'business_name': forms.TextInput(attrs={'class': 'unicorn'}),
            'business_type': forms.Select(attrs={'class': 'unicorn', 'style': "width:340px"}),
            'tax_id': forms.TextInput(attrs={'class': 'unicorn'}),
            'phone': forms.TextInput(attrs={'class': 'unicorn', 'placeholder': '( )___ ___ __ __'}),
            'address': forms.Textarea(attrs={'class': 'unicorn', 'style': "background:#f6f6f6"}),
            'information': forms.Textarea(attrs={'class': 'unicorn', 'style': "background:#f6f6f6"}),
        }

class PetLoverUserCreationForm(UserCreationForm):
    class Meta:
        model = PetLover
        fields = ['username', 'full_name', 'email', 'password1', 'password2', 'location',
                  'tckn', 'phone', 'birthDate', 'gender', 'profile_image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'unicorn'}),
            'full_name': forms.TextInput(attrs={'class': 'unicorn'}),
            'email': forms.TextInput(attrs={'class': 'unicorn'}),
            'password1': forms.PasswordInput(attrs={'class': 'unicorn', 'type': 'password2'}),
            'password2': forms.PasswordInput(attrs={'class': 'unicorn', 'type': 'password2'}),
            'address': forms.Textarea(attrs={'class': 'unicorn', 'style': 'width:328px'}),
            'tckn': forms.TextInput(attrs={'class': 'unicorn'}),
            'phone': forms.TextInput(attrs={'class': 'unicorn', 'placeholder': '( )___ ___ __ __'}),
            'birthDate': forms.DateInput(attrs={'class': 'unicorn', 'type': 'date', 'max': datetime.now().date()}),
            'gender': forms.Select(attrs={'class': 'unicorn', 'style': 'width: 324px; background-color: #f6f6f6'}),
        }

class PetCreationForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['type', 'name', 'race', 'height', 'weight', 'birthDate', 'gender',
                  'pet_image']
        widgets = {
            'type': forms.Select(attrs={'class': 'unicorn', 'style': "width:340px ; background-color: #f6f6f6'"}),
            'name': forms.TextInput(attrs={'class': 'unicorn'}),
            'race': forms.TextInput(attrs={'class': 'unicorn'}),
            'height': forms.TextInput(attrs={'class': 'unicorn'}),
            'weight': forms.TextInput(attrs={'class': 'unicorn'}),
            'birthDate': forms.DateInput(attrs={'class': 'unicorn', 'type': 'date', 'max': datetime.now().date()}),
            'gender': forms.Select(attrs={'class': 'unicorn', 'style': "width:340px; background-color: #f6f6f6'"}),
        }


