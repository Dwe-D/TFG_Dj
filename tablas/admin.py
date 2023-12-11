from django.contrib import admin
from bd_masfilas.models import teclado

class tecladoAdmin(admin.ModelAdmin):
    list_display=("id","numero1", "numero2", "numero3", "numeroB")

admin.site.register(teclado, tecladoAdmin)