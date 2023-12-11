from django.contrib import admin
from bd_masfilas.models import teclado
from .models import UsuarioArduino, DatosDispositivo

class tecladoAdmin(admin.ModelAdmin):
    list_display=("id","numero1", "numero2", "numero3", "numeroB")

class userAD(admin.ModelAdmin):
    list_display=("usuario","dispositivo_id", "alias")

class DatosAdmin(admin.ModelAdmin):
    list_display = ("mostrar_dispositivo_id", "fecha_creacion", "temp", "hum")

    def mostrar_dispositivo_id(self, obj):
        return obj.dispositivo.dispositivo_id

    mostrar_dispositivo_id.short_description = "Dispositivo ID"  # Define un nombre más amigable para la columna

admin.site.register(DatosDispositivo, DatosAdmin)

admin.site.register(teclado, tecladoAdmin)
admin.site.register(UsuarioArduino, userAD)
