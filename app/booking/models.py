from django.db import models

# Create your models here.

class Booking(models.Model):

    user = models.ForeignKey('register.User', on_delete=models.CASCADE, related_name='user')
    service = models.CharField(max_length=100)
    practitioner_id = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name