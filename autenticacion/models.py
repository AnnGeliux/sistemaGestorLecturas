from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Usuario(AbstractUser):
    nombre = models.CharField(max_length=150)
    correo_electronico = models.EmailField(unique=True)

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['username', 'nombre']

    def __str__(self):
        return self.nombre

