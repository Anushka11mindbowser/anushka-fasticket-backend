from django.db import models
from bookings.models import Bookings

# Create your models here.
class Seats(models.Model):
    seat_number = models.CharField(max_length=5, blank=False, null=True)
    booking_id = models.ForeignKey(Bookings, on_delete=models.CASCADE)