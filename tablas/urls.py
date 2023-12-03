from django.urls import path
from .views import tabla, webhook
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tabla, name="tabla"),
    path('deco', webhook, name="deco" )

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)