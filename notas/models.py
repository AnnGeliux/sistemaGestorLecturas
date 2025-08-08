from django.db import models
from libros.models import Libro

from django.conf import settings

class Nota(models.Model):
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    hora_creacion = models.TimeField(auto_now_add=True, null=True, blank=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='notas')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notas', null=True, blank=True)

    def __str__(self):
        return f"Nota de {self.libro.titulo} - {self.fecha} {self.hora_creacion} por {self.autor}" 
