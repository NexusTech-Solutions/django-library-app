from django.db import models

class book():
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    year = models.CharField(max_length=4)

