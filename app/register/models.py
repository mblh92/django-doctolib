from django.db import models


# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
