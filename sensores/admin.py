from django.contrib import admin
from .models import UsuarioDispositivo, Datos

class userAD(admin.ModelAdmin):
    list_display=("usuario","dispositivo_id", "alias")

class DatosAdmin(admin.ModelAdmin):
    list_display = ("mostrar_dispositivo_id", "fecha_creacion", "temp", "hum","limo", "detec")

    def mostrar_dispositivo_id(self, obj):
        return obj.dispositivo.dispositivo_id

    mostrar_dispositivo_id.short_description = "Dispositivo ID"  # Define un nombre más amigable para la columna

admin.site.register(Datos, DatosAdmin)
admin.site.register(UsuarioDispositivo, userAD)
