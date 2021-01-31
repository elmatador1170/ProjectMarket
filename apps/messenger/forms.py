from django import forms
from .models import Message
from django.contrib.auth import get_user_model


class Messaging(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['title', 'content', 'recipient']
        labels = {'title': 'Betreff', 'content': 'Nachricht', 'recipient': 'Empfänger'}

