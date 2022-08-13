from dataclasses import fields
from rest_framework import serializers
from .models import (
                    Movies,
                    Plays
)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'

class PlaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plays
        fields = '__all__'

