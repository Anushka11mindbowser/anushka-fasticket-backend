from pyexpat import model
from rest_framework import serializers
from .models import Bookings

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ['name', 'email', 'phone', 'booked_show', 'booked_at', 'show_date', 'show_time', 'show_theatre', 'ticket_quantity']



