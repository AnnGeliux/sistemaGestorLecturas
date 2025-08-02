from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from libros.models import Libro

class ProgresoLectura(models.Model):
    libro = models.OneToOneField(Libro, on_delete=models.CASCADE, related_name='progreso')
    ultima_pagina_leida = models.PositiveIntegerField(verbose_name='Última página leída')
    porcentaje_avance = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name='Porcentaje de avance'
    )

    def save(self, *args, **kwargs):
        if self.libro.numero_paginas > 0:
            avance = (self.ultima_pagina_leida / self.libro.numero_paginas) * 100
            self.porcentaje_avance = round(avance, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Progreso en '{self.libro.titulo}': {self.porcentaje_avance}% (página {self.ultima_pagina_leida})"