from django import forms
from django.forms import ModelForm

from .models import Services
from register.models import User


class ServiceForm(ModelForm):
    class Meta:
            model = Services
            fields = ['name', 'description']
            widgets = {
                'name': forms.TextInput(attrs={
                        'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                        'placeholder': 'Nom de mon service...'
                    }),

                'description': forms.Textarea(attrs={
                        'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                        'placeholder': 'Voici mon service...'
                    })
            }


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'addressCabinet', 'phoneCabinet', 'description', 'age']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-400 p-2 mt-2 mb-3',
                'placeholder': 'Prénom',
                'readonly':'readonly'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-400 p-2 mt-2 mb-3',
                'placeholder': 'Nom',
                'readonly':'readonly'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-400 p-2 mt-2 mb-3',
                'placeholder': 'Email',
                'readonly':'readonly'
            }),

            'username': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                'placeholder': 'Pseudo'
            }),

            'addressCabinet': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                'placeholder': 'Adresse du cabinet'
            }),

            'phoneCabinet': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                'placeholder': '+33 1 45 85 41 25'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                'placeholder': '35 ans',
                'min': '18',
                'max': '99'
            }),

            'description': forms.Textarea(attrs={
                'class': 'w-full bg-gray-100 p-2 mt-2 mb-3',
                'placeholder': 'Je suis un psychologue...'
            })
        }