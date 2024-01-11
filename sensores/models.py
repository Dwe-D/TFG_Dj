from django.db import models
from django.contrib.auth.models import User

class UsuarioDispositivo(models.Model):
    usuario = models.ForeignKey(User, related_name='dispositivos', on_delete=models.CASCADE)
    dispositivo_id = models.CharField(max_length=50, unique=True)
    alias = models.CharField(max_length=50, blank=True, null=True)

class Datos(models.Model):
    dispositivo = models.ForeignKey(UsuarioDispositivo, on_delete=models.CASCADE, related_name='datos_dispositivos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    temp = models.FloatField()
    hum = models.FloatField()
    ppm = models.FloatField()
    lemo = models.BooleanField()