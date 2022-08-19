from dataclasses import fields
from rest_framework import serializers
from .models import (
                    Movies,
                    Plays
)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id','movie_name', 'movie_genre', 'movie_time', 'movie_poster', 'movie_language']

class PlaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plays
        fields = ['play_name', 'play_genre', 'play_duration', 'play_poster', 'play_language']

