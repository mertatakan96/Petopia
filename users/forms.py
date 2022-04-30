from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Business

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
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control'}),
            'business_type': forms.Select(attrs={'class': 'form-select', 'style': "width:250px"}),
            'tax_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '( )___ ___ __ __'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'style': "background:#f6f6f6"}),
            'information': forms.Textarea(attrs={'class': 'form-control', 'style': "background:#f6f6f6"}),
        }

