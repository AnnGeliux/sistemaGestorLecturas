from django.db import models
from libros.models import Libro

class MetaLectura(models.Model):
    TIPOS = [
        ('mensual', 'Mensual'),
        ('anual', 'Anual'),
    ]

    nombre = models.CharField(max_length=200)
    creador = models.ForeignKey('autenticacion.Usuario', on_delete=models.CASCADE, related_name='metas_creadas', null=True, blank=True, help_text='Usuario que creó la meta')
    tipo = models.CharField(max_length=10, choices=TIPOS)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    libros_asociados = models.ManyToManyField(Libro, related_name='metas')
    usuarios_asignados = models.ManyToManyField('autenticacion.Usuario', related_name='metas_asignadas', blank=True, help_text='Usuarios a los que se asigna esta meta')
    porcentaje_avance = models.DecimalField(max_digits=5, decimal_places=2, default=0, null=False, blank=True)

    def __str__(self):
        return self.nombre
