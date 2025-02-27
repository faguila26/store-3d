# models/shelf.py
from django.db import models

class Shelf(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100) 

    def __str__(self):
        return self.name


