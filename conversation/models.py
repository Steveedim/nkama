from django.db import models
from django.contrib.auth.models import User

from flex.models import Product


class Conversation(models.Model):
    item = models.ForeignKey(Product, related_name="conversations", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-modified_at"]

        def __str__(self):
            return self.members


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created_at


