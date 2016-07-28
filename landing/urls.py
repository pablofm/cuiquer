from django.conf.urls import url
from landing.views import Index, Cuiquer, CondicionesPrivacidad, CondicionesUso, Cookies

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^cuiquer$', Cuiquer.as_view(), name='cuiquer'),
    url(r'^cookies$', Cookies.as_view(), name='cookies'),
    url(r'^condiciones_uso$', CondicionesUso.as_view(), name='condiciones_uso'),
    url(r'^condiciones_privacidad$', CondicionesPrivacidad.as_view(), name='condiciones_privacidad'),
]
