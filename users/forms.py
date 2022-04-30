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

