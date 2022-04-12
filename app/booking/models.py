from django.db import models
from register.models import User
from account.models import Services


# Create your models here.

class Booking(models.Model):

    user = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='user')
    practitioner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='practitioner')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='service')
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name