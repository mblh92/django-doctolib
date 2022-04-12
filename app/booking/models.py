from django.db import models
from register.models import User
from account.models import Services
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Booking(models.Model):

    user = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='user')
    practitioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='practitioner')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service')
    phone = PhoneNumberField(max_length=100)
    date = models.DateField()
    time = models.TimeField()