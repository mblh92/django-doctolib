# coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    PROFESSIONAL = 'PROFESSIONAL'
    PARTICULAR = 'PARTICULAR'
    ROLE_CHOICES = (
        (PROFESSIONAL, 'Pro'),
        (PARTICULAR, 'Particulier'),
    )

    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

