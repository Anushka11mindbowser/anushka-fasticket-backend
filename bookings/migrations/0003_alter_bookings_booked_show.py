# Generated by Django 4.1 on 2022-08-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_bookings_show_date_bookings_show_theatre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='booked_show',
            field=models.CharField(max_length=255),
        ),
    ]