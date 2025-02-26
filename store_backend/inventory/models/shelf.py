# models/shelf.py
from django.db import models

class Shelf(models.Model):
    # Ejemplo de un modelo con un campo location
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    # Si location no está definido, este campo será inválido.
    location = models.CharField(max_length=100)  # Asegúrate de que exista este campo si es necesario

    def __str__(self):
        return self.name


