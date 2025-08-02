from django.db import models
from libros.models import Libro

class Nota(models.Model):
    contenido = models.TextField()
    fecha = models.DateField(auto_now_add=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='notas')

    def __str__(self):
        return f"Nota de {self.libro.titulo} - {self.fecha}"
