from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    ESTADOS = [
        ('por_leer', 'Por leer'),
        ('leyendo', 'Leyendo'),
        ('leido', 'Leído'),
    ]

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=100)
    numero_paginas = models.PositiveIntegerField()
    estado = models.CharField(max_length=10, choices=ESTADOS, default='por_leer')
    porcentaje_avance = models.PositiveIntegerField(default=0, help_text="Porcentaje de avance de lectura (0-100)")
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, related_name='libros')
    etiquetas = models.ManyToManyField(Etiqueta, related_name='libros')
    fecha_publicacion = models.DateField(null=True, blank=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='libros')
    imagen = models.ImageField(upload_to='libros_portadas/', null=True, blank=True, verbose_name='Portada')



    def __str__(self):
        return self.titulo


    def avance_lectura(self):
        return self.porcentaje_avance or 0