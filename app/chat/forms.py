from django import forms
from django.forms import ModelForm

from .models import Chat


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['message']
        widgets = {
            'message': forms.TextInput(
                attrs={
                    'class': 'flex-grow m-2 py-2 px-4 mr-1 w-11/12 rounded-full border border-gray-300 bg-gray-200 resize-none',
                    'placeholder': 'Votre numéro de téléphone',
                })}
