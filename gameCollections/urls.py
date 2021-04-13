from django.urls import path
from . import views

app_name = 'gameCollections'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('gameCollections/', views.genres, name = 'genres'),
    path('<int:genre_id>/games/', views.games, name = 'games'),

    path('new_genre/', views.new_genre, name = 'new_genre'),
    path('new_game/<int:genre_id>/', views.new_game, name='new_game'),
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
]