from django.db import models

# Create your models here.
class Bookings(models.Model):
    booking_id = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    booked_show = models.CharField(max_length=5)
    booked_at = models.DateTimeField()


    