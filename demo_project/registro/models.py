from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} - {self.cedula}"
