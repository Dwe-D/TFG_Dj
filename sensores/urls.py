from django.urls import path
from .views import tabla, webhook, reg, meter, deco, eliminar_dispositivos, listar_dispositivos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('visualizar', tabla, name="datos"),
    path('webhook', webhook, name="webhook" ),
    path('registrar', reg, name="reg" ),
    path('eliminar_dispositivos', eliminar_dispositivos, name="eliminar_dispositivos" ),
    path('eliminar', listar_dispositivos, name="elimina" ),
    path('deco', deco, name="deco" ),
    path('meter', meter, name="meter" )
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
