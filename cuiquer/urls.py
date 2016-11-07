from django.conf.urls import url, include
from django.contrib import admin
from landing import urls as landing_urls
from profesionales import urls as profesionales_urls
from clientes import urls as clientes_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(landing_urls)),
    url(r'^profesionales/', include(profesionales_urls)),
    url(r'^clientes/', include(clientes_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
