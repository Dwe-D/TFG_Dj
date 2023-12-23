from django.urls import path
from .views import VRegistro, cerrar_sesion, logear, eliminar_usuario
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('singup', VRegistro.as_view(), name="singup"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('', logear, name="login"),
    path('eliminar_usuario/', eliminar_usuario, name='eliminar_usuario'),
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)