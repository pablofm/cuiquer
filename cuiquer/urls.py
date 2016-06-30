from django.conf.urls import url, include
from django.contrib import admin
from landing import urls as landing_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(landing_urls)),
]
