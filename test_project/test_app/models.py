from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)


class Cinema(models.Model):
    cinema_location = models.CharField(max_length=200)
    movies_on_currently = models.ManyToManyField(Movie)

