"""
This file contains forms used for user login.
"""

# -----------------------------------------------------------------------------------------------------------------------------------------
#       IMPORTS                 
# -----------------------------------------------------------------------------------------------------------------------------------------
from django import forms
from .models import User
from django.core.validators import EmailValidator

# -----------------------------------------------------------------------------------------------------------------------------------------
#       LOGIN FORM          
# -----------------------------------------------------------------------------------------------------------------------------------------
class LoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
        'placeholder': 'email...',
    }), validators=[EmailValidator()])

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'placeholder': 'password...',
    }))
    
    class Meta:
        model = User
        fields = {
            'email',
            'password'
             #do not include ids
        }
class registerForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'id': 'email',
        'placeholder': 'Email address',
    }), validators=[EmailValidator()])

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id': 'password',
        'placeholder': 'Password',
    }))
    image = forms.ImageField(required = False)
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "placeholder": "Username"
    }))
    class Meta:
        model = User
        fields = {
            'email',
            'password',
            'image',
            'username'
        }