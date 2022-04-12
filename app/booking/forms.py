from django import forms
from django.forms import ModelForm

from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['phone', 'service', 'date', 'time']
        # widgets = {
        #     'phone': forms.TextInput(
        #         attrs={
        #             'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
        #             'placeholder': 'Votre numéro de téléphone',
        #         }),
        #     'service': forms.TextInput(
        #         attrs={
        #             'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
        #             'placeholder': 'Your Name'
        #         }),
        #     'practitioner_id': forms.TextInput(
        #         attrs={
        #             'label': 'Praticien',
        #             'rows': 3,
        #             'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
        #             'placeholder': 'Hello Roylan,'
        #         }),
        #     'date': forms.TextInput(
        #         attrs={
        #             'rows': 3,
        #             'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
        #             'placeholder': 'Hello Roylan,'
        #         }),
        #     'time': forms.TextInput(
        #         attrs={
        #             'rows': 3,
        #             'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm',
        #             'placeholder': 'Hello Roylan,'
        #         }),
        #
        # }
