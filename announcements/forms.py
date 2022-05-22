from django.forms import ModelForm
from django import forms
from .models import FoundedPet, AdoptPet, LostPet

class FoundedPetCreationForm(ModelForm):
    class Meta:
        model = FoundedPet
        fields = ['pet_image', 'title', 'type', 'gender', 'phone', 'info', 'address']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
        }

class AdoptPetCreationForm(ModelForm):
    class Meta:
        model = AdoptPet
        fields = ['pet_image', 'title', 'type', 'gender', 'phone', 'info', 'address']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
        }

class LostPetCreationForm(ModelForm):
    class Meta:
        model = LostPet
        fields = ['pet_image', 'title', 'type', 'gender', 'phone', 'info', 'address']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
        }