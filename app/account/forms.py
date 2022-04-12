from django import forms
from django.forms import ModelForm

from .models import Services


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
                        'placeholder': 'Nom de mon service...'
                    })
            }