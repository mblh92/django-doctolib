from django.db import models

class Services(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    description = models.CharField(max_length=255, verbose_name='description')
    user = models.ForeignKey('register.User', on_delete=models.CASCADE)
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey('register.User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name