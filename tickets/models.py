from django.db import models

# Create your models here.
class Tickets(models.Model):
    ticket_id = models.CharField(max_length=5)
    seat_number = models.CharField(max_length=5)
    