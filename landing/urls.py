from django.conf.urls import url
from landing.views import Index, Cuiquer

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^cuiquer$', Cuiquer.as_view(), name='cuiquer'),
]
