# Generated by Django 4.1.3 on 2024-02-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=100)),
                ("Release_Date", models.DateField()),
                ("Genre", models.CharField(max_length=100)),
                ("Language", models.CharField(max_length=100)),
                ("Duration", models.CharField(max_length=100)),
                ("Director", models.CharField(max_length=100)),
                ("Cast", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("Description", models.TextField()),
                ("Category", models.CharField(max_length=100)),
                (
                    "Poster",
                    models.ImageField(blank=True, null=True, upload_to="movie_posters"),
                ),
            ],
        ),
    ]
