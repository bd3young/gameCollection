from django.urls import path
from . import views

app_name = 'gameCollections'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('gameCollections/', views.genres, name = 'genres'),
    path('<int:genre_id>/games/', views.games, name = 'games'),
]