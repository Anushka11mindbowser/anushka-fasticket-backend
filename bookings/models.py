from datetime import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Bookings(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    email = models.CharField(max_length=255, blank=False, null=True)
    phone = models.CharField(max_length=255, blank=False, null=True)
    show = models.CharField(max_length=255, blank=False, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    seat_nos = ArrayField(ArrayField(models.CharField(max_length=5, blank=False, null=True)))

    def __str__(self):
        return self.name

   
    