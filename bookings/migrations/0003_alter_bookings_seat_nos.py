# Generated by Django 4.1 on 2022-08-22 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_bookings_seat_nos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='seat_nos',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
