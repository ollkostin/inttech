from django.db import models


class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
