from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.conf import settings
from datetime import date
from django.contrib.auth.models import User


class CreateUser(UserCreationForm):
    """Das Django Standard-Formular für Registrierungen wird hier erweitert"""
    first_name = forms.CharField(label='Vorname', max_length=30)
    last_name = forms.CharField(label='Nachname', max_length=30)
    birthday = forms.DateField(label='Geburtsdatum', initial=date.today)
    email = forms.EmailField(label='E-Mail', max_length=254)

    def __init__(self, *args, **kwargs):
        super(CreateUser, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

        self.fields['password1'].label = 'Passwort'
        self.fields['password2'].label = 'Passwort bestätigen'

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'username',
            'password1',
            'password2'
        ]

        labels = {
            'username': 'Benutzername',
            'first_name': 'Name',
            'last_name': 'Nachname',
            'birthday': 'Geburtstag',
            'email': 'E-Mail',
            'password1': 'Passwort',
            'password2': 'Passwort bestätigen'
        }

        widgets = {
            'first_name': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'username': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control'
            })
        }


class UpdateInformation(UserChangeForm):
    """Formular zur Aktualisierung der Kontoinformationen."""
    first_name = forms.CharField(label='Vorname', max_length=30)
    last_name = forms.CharField(label='Nachname', max_length=30)
    birthday = forms.DateField(label='Geburtsdatum', initial=date.today)
    email = forms.EmailField(label='E-Mail', max_length=254)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'username',
        ]
