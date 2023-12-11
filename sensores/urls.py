from django.urls import path
from .views import tabla, webhook, reg, meter, deco
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', tabla, name="tabla"),
    path('webhook', webhook, name="webhook" ),
    path('reg', reg, name="reg" ),
    path('deco', deco, name="deco" ),
    path('meter', meter, name="meter" )
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
