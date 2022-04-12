from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    description = models.CharField(max_length=255, verbose_name='description')
    user = models.ForeignKey('register.User', on_delete=models.CASCADE)