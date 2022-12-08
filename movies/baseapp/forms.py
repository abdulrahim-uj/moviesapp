from django import forms
from django.forms import TextInput, ClearableFileInput, Textarea
from django.utils.translation import gettext_lazy as _
from . models import Movies


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name', 'year', 'poster', 'description']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control',
                                     'placeholder': ''}),
            'year': TextInput(attrs={'class': 'required form-control',
                                     'placeholder': '', 'type': 'number'}),
            'poster': ClearableFileInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'required form-control', 'rows': '5',
                                     'placeholder': ''}),
        }
        error_messages = {
            'name': {
                'required': _("This field is required"),
            },
            'year': {
                'required': _("This field is required"),
            },
            'description': {
                'required': _("This field is required"),
            },
        }
        labels = {
            "name": "Movie Name",
            "year": "Release Year",
            "poster": "Movie Poster",
            "description": "Brief Story",
        }
