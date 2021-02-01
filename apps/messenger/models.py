from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Conversation(models.Model):
    """Model für eine Konversation."""
    date_started = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Message(models.Model):
    """Nachricht wird erfasst."""
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    users = get_user_model().objects.all()
    CHOOSE_RECIPIENT = [(user.username, user.username) for user in users]

    recipient = models.CharField(max_length=100, choices=CHOOSE_RECIPIENT, default=CHOOSE_RECIPIENT[1])

    def __str__(self):
        return self.content[:50]


class Participator(models.Model):
    """Benutzername der Teilnehmer einer Konversation wird erfasst."""
    conversations = models.ManyToManyField(Conversation)
    username = models.CharField(max_length=100)
