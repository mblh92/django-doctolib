from django.db import models


# Create your models here.
class Chat(models.Model):
    message = models.CharField(max_length=255)
    register_user = 'register.User'
    user = models.ForeignKey(register_user, related_name='user', on_delete=models.CASCADE)
    sender = models.ForeignKey(register_user, related_name='sender', on_delete=models.CASCADE)
    sender_current_message = models.ForeignKey(register_user, related_name='sender_current_message', on_delete=models.CASCADE)
