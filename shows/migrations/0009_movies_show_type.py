# Generated by Django 4.1 on 2022-08-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0008_remove_movies_movie_id_remove_plays_play_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='show_type',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
