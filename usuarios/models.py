from django.db import models
#from django.db import models

class Usuario(models.Model):
    dni = models.IntegerField(unique=True)
    apellidos = models.CharField(max_length=250)
    nombres = models.CharField(max_length=300)
    correo = models.EmailField(max_length=300)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    telefono = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# Create your models here.
