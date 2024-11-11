from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User




class User(AbstractUser):
    # Additional fields for all users
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_client_info = models.TextField()

class ManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    additional_manager_info = models.TextField()


class Notifications(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_notifications")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_notifications")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notifications from {self.sender} to {self.receiver}"
