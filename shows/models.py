from django.db import models

# Create your models here.

class Movies(models.Model):
    movie_id = models.CharField(max_length=5, unique=True)
    movie_name = models.CharField(max_length=500)
    movie_genre = models.CharField(max_length=255)
    movie_time = models.TimeField()
    movie_poster = models.CharField(max_length=750)
    
    
class Plays(models.Model):
    play_id =  models.CharField(max_length=5, unique=True)
    play_name = models.CharField(max_length=255)
    play_genre = models.CharField(max_length=255)
    play_duration = models.CharField(max_length=255)
    play_poster = models.CharField(max_length=750)