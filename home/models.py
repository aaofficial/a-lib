from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField()
    grade = models.CharField(max_length=200)