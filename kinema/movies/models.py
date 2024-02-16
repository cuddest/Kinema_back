from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Movie(models.Model):
    Title = models.CharField(max_length=100)
    Release_Date = models.DateField()
    Genre = models.CharField(max_length=100)
    Language = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    Director = models.CharField(max_length=100)
    Cast = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    Description = models.TextField()
    Category = models.CharField(max_length=100)
    Poster = models.ImageField(upload_to="movie_posters", blank=True, null=True)

    def __str__(self):
        return self.Title


# Create your models here.
