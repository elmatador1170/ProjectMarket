from django import forms
from .models import Project, Review


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'short_description', 'is_private']
        labels = {'title': 'Projektname', 'short_description': 'Beschreibung', 'is_private': 'Privat'}
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'short_description': forms.TextInput(attrs={
                'class': 'form-control'
            })
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
        labels = {'text': 'Kommentar', 'rating': 'Bewertung'}
