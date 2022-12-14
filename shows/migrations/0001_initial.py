# Generated by Django 4.1 on 2022-08-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(max_length=5, unique=True)),
                ('movie_name', models.CharField(max_length=500)),
                ('movie_genre', models.CharField(max_length=255)),
                ('movie_time', models.TimeField()),
                ('movie_poster', models.CharField(max_length=750)),
            ],
        ),
        migrations.CreateModel(
            name='Plays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('play_id', models.CharField(max_length=5, unique=True)),
                ('play_name', models.CharField(max_length=255)),
                ('play_genre', models.CharField(max_length=255)),
                ('play_duration', models.CharField(max_length=255)),
                ('play_poster', models.CharField(max_length=750)),
            ],
        ),
    ]
