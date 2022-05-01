from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from .models import User

class BusinessCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'business_name',
                          'business_type', 'tax_id', 'phone', 'address', 'information']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'unicorn'}),
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
        model = User
        fields = ['username', 'email', 'full_name', 'password1', 'password2', 'location', 'tckn', 'phone', 'birthDate', 'gender']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'unicorn'}),
            'full_name': forms.TextInput(attrs={'class': 'unicorn'}),
            'email': forms.TextInput(attrs={'class': 'unicorn'}),
            'password1': forms.PasswordInput(attrs={'class': 'unicorn', 'type': 'password2'}),
            'password2': forms.PasswordInput(attrs={'class': 'unicorn', 'type': 'password2'}),
            'location': forms.TextInput(attrs={'class': 'unicorn'}),
            'tckn': forms.TextInput(attrs={'class': 'unicorn'}),
            'phone': forms.TextInput(attrs={'class': 'unicorn', 'placeholder': '( )___ ___ __ __'}),
            'birthDate': forms.DateInput(attrs={'class': 'unicorn', 'type': 'date', 'max': datetime.now().date()}),
            'gender': forms.Select(attrs={'class': 'unicorn', 'style': 'width: 324px; background-color: #f6f6f6'}),
        }

