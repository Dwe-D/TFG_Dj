from django.urls import path
from .views import tabla, procesar_datos_ttn
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tabla, name="tabla"),
    path('deco', procesar_datos_ttn, name="deco" )

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)