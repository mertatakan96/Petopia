from django.forms import ModelForm
from django import forms
from .models import FoundedPet, AdoptPet, LostPet, FoundedPetComment, AdoptPetComment, LostPetComment

class FoundedPetCreationForm(ModelForm):
    class Meta:
        model = FoundedPet
        fields = ['pet_image', 'title', 'type', 'gender', 'phone', 'info', 'city']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
        }

class AdoptPetCreationForm(ModelForm):
    class Meta:
        model = AdoptPet
        fields = ['pet_image', 'title', 'type', 'gender', 'phone', 'info', 'city']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
        }

class LostPetCreationForm(ModelForm):
    class Meta:
        model = LostPet
        fields = ['pet_image', 'title', 'type', 'gender', 'phone', 'info', 'city']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
            'gender': forms.Select(attrs={'class': 'form-control', 'style': "width:370px"}),
        }

class FoundedCommentForm(ModelForm):
    class Meta:
        model = FoundedPetComment
        fields = ['body']

class AdoptCommentForm(ModelForm):
    class Meta:
        model = AdoptPetComment
        fields = ['body']

class LostCommentForm(ModelForm):
    class Meta:
        model = LostPetComment
        fields = ['body']