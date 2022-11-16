from unittest.util import _MAX_LENGTH
from django.db import models



class Maquina(models.Model):

    codigo = models.CharField(max_length=100)
    modelo = models.CharField(max_length = 100)
    operador = models.CharField(max_length = 100)
    estado = models.CharField(max_length = 100)

    def __str__(self):
        return self.modelo


class Clientes(models.Model):
    rut = models.CharField(max_length = 10)
    nombre = models.CharField(max_length = 100)
    apellido = models.CharField(max_length = 100)
    fecha = models.CharField(max_length=100)
    monto= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class inicio(models.Model):
    rut = models.CharField(max_length=10)
    clave = models.CharField (max_length=8)

    def __str__(self):
        return self.rut



        
# Create your models here.
