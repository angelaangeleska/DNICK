from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PublishingHouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    country = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return self.name + " " + self.surname


class Book(models.Model):
    isbn = models.IntegerField()
    title = models.CharField(max_length=100)
    summary = models.TextField()
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ", " + self.author.name + " " + self.author.surname


class PublishingHouseAuthor(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.publishing_house.name + ", " + self.author.name