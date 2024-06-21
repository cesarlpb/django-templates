from django.db import models

class MiUser(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=3) # a veces aparece warning: quitar max_length
    es_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Mi Usuario"
        verbose_name_plural = "Mis Usuarios"

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"