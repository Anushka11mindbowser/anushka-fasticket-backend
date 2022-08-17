from django.db import models

# Create your models here.

class Movies(models.Model):
   
    movie_name = models.CharField(max_length=500, blank=False, null=True)
    movie_genre = models.CharField(max_length=255, blank=False, null=True)
    movie_time = models.DurationField(blank=False, null=True)
    movie_poster = models.CharField(max_length=750, blank=False, null=True)
    movie_language = models.CharField(max_length=11, blank=False, null=True)
    
    
    
class Plays(models.Model):
    play_name = models.CharField(max_length=255, blank=False, null=True)
    play_genre = models.CharField(max_length=255, blank=False, null=True)
    play_duration = models.DurationField(max_length=255, blank=False, null=True)
    play_poster = models.CharField(max_length=750, blank=False, null=True)
    play_language = models.CharField(max_length=11, blank=False, null=True)