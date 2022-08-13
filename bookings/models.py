from datetime import datetime
from django.db import models

# Create your models here.
class Bookings(models.Model):
    booking_id = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    booked_show = models.CharField(max_length=255)
    booked_at = models.DateTimeField(auto_now_add=True)
    show_date = models.DateField(default=datetime.now, blank=True)
    show_time = models.TimeField(default=datetime.now, blank=True)
    show_theatre = models.CharField(max_length=255, blank=True)
    ticket_quantity = models.IntegerField(default = 0, blank=True)

    def __str__(self):
        return self.name
    