from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client_reports")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.client.username} - {self.title}"
