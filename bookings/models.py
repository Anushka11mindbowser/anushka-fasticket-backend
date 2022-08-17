from datetime import datetime
from django.db import models

# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=255, blank=False, null=True)
    phone = models.CharField(max_length=255, blank=False, null=True)
    booked_show = models.CharField(max_length=255, blank=False, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    show_date = models.DateField(default=datetime.now, blank=False, null=True)
    show_time = models.TimeField(default=datetime.now, blank=False, null=True)
    show_theatre = models.CharField(max_length=255, blank=False, null=True)
    ticket_quantity = models.IntegerField(default = 0, blank=False, null=True)

    def __str__(self):
        return self.name
    