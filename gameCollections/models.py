from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Game(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    console = models.CharField(max_length=200)
    releaseDate = models.DateField()
 
    class Meta:
        verbose_name_plural = 'games'

    def __str__(self):
        return self.name