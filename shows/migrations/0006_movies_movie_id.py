# Generated by Django 4.1 on 2022-08-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0005_alter_movies_movie_genre_alter_movies_movie_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movie_id',
            field=models.CharField(max_length=5, null=True, unique=True),
        ),
    ]
