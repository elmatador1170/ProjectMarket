from django import forms
from .models import Message
from django.contrib.auth import get_user_model


class Messaging(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'recipient']
        labels = {'title': 'Betreff', 'content': 'Nachricht', 'recipient': 'Empfänger'}

        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'content': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }


class ChatMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        labels = {'content': 'Nachricht'}
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control'
            })
        }