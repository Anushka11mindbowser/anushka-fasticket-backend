# Generated by Django 4.1 on 2022-08-15 20:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_bookings_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booked_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='booked_show',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='email',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='show_date',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='show_theatre',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='show_time',
            field=models.TimeField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='bookings',
            name='ticket_quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
