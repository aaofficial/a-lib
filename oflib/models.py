from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    adddate = models.DateField()

class Libmembers(models.Model):
  name = models.CharField(max_length=255)
  grade = models.IntegerField()
  joindate = models.DateField()