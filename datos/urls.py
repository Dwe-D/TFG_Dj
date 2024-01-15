from django.urls import path
from django.conf import settings
from .views import tabla, tabla_DF, listar_DF, listar_PPM, tabla_PPM, tabla_DPPM, listar_DPPM, listar_D, tabla_D, listar_F, tabla_F
from django.conf.urls.static import static

urlpatterns = [
    path('visualizar', tabla, name="datos"),
    path('tablaDF', tabla_DF, name="tablaDF"),
    path('list_PPM', listar_PPM, name="list_PPM"),
    path('tablaPPM', tabla_PPM, name="tablaPPM"),
    path('tablaDPPM', tabla_DPPM, name="tablaDPPM"),
    path('list_DF', listar_DF, name="list_DF" ),
    path('list_DPPM', listar_DPPM, name="list_DPPM" ),
    path('list_D', listar_D, name="list_D" ),
    path('tablaD', tabla_D, name="tablaD" ),
    path('list_F', listar_F, name="list_F" ),
    path('tablaF', tabla_F, name="tablaF" ),

]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
