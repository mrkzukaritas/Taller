from django.db import models

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField(null=True, blank=True)
    prioridad = models.IntegerField(default=1)
    categoria = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.titulo