from django.shortcuts import render
from .models import Genre, Game 

def index(request):
        return render(request, 'gameCollections/index.html')

def genres(request):
    genres = Genre.objects.all()
    context = {'genres' : genres}
    return render (request, 'gameCollections/genres.html', context)

def games(request, genre_id):
    genre = Genre.objects.get(id = genre_id)
    games = genre.game_set.order_by('-releaseDate')
    context = {'genre' : genre, 'games' : games}
    return render (request, 'gameCollections/games.html', context)
