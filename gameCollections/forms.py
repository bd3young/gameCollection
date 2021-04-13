from django import forms
from .models import Genre, Game

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
        labels = {'name': ''}

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'console', 'releaseDate']
        labels = {'name': 'Game', 'console': 'Console', 'releaseDate': 'Realease Date' }