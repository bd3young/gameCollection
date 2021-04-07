from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Game(models.Model):
    pizza = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.TextField()
    console = models.TextField()
    releaseDate = models.DateField()
 
    class Meta:
        verbose_name_plural = 'games'

    def __str__(self):
        return self.name