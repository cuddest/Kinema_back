# Generated by Django 4.1.3 on 2024-03-17 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0003_rename_title_movie_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="movie",
            old_name="Director",
            new_name="production_companies",
        ),
    ]
