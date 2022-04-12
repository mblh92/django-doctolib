# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    PROFESSIONAL = 'PROFESSIONAL'
    PARTICULAR = 'PARTICULAR'
    ROLE_CHOICES = (
        (PROFESSIONAL, 'Pro'),
        (PARTICULAR, 'Particulier'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')
    addressCabinet = models.CharField(max_length=255, verbose_name='Adresse du cabinet', null=True, default=None, blank=True)
    phoneCabinet = PhoneNumberField(blank=True, null=True, verbose_name='Téléphone du cabinet')
    age = models.IntegerField(verbose_name='Age', null=True, default=None, blank=True)
    description = models.TextField(verbose_name='Description', null=True, default=None, blank=True)

