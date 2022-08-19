from pyexpat import model
from rest_framework import serializers
from .models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['id','name', 'email', 'phone', 'show', 'booked_at', 'seat_nos']



