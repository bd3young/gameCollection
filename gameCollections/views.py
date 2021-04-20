from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Genre, Game
from .forms import GenreForm, GameForm

def index(request):
        return render(request, 'gameCollections/index.html')

@login_required
def genres(request):
    genres = Genre.objects.filter(owner=request.user).order_by('name')
    context = {'genres' : genres}
    return render (request, 'gameCollections/genres.html', context)

@login_required
def games(request, genre_id):
    genre = Genre.objects.get(id = genre_id)

    if genre.owner != request.user:
        raise Http404

    games = genre.game_set.order_by('-releaseDate')
    context = {'genre' : genre, 'games' : games}
    return render (request, 'gameCollections/games.html', context)

@login_required
def new_genre(request):
    """Add a new genre."""
    if request.method != 'POST':
        form = GenreForm()

    else:
        form = GenreForm(data=request.POST)
        if form.is_valid():
            new_genre = form.save(commit=False)
            new_genre.owner = request.user
            new_genre.save()
            return redirect('gameCollections:genres')

    context = {'form': form}
    return render(request, 'gameCollections/new_genre.html', context)

@login_required
def new_game(request, genre_id):
    """Add a new game for a particular genre."""
    genre = Genre.objects.get(id=genre_id)
 
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GameForm()
    else:
        # POST data submitted; process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.genre = genre
            new_game.save()
            return redirect('gameCollections:games', genre_id=genre_id)
    # Display a blank or invalid form.
    context = {'genre': genre, 'form': form}
    return render(request, 'gameCollections/new_game.html', context)

@login_required
def edit_game(request, game_id):
    """Edit an existing Game."""
    game = Game.objects.get(id=game_id)
    genre = game.genre 
    if genre.owner != request.user:
        raise Http404
 
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = GameForm(instance=game)
    else:
        # POST data submitted; process data.
        form = GameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('gameCollections:games', genre_id=genre.id)
    context = {'game': game, 'genre': genre, 'form': form}
    return render(request, 'gameCollections/edit_game.html', context)