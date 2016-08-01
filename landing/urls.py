from django.conf.urls import url
from landing import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^newsletter$', views.newsletter, name='newsletter'),
    url(r'^cuiquer$', views.Cuiquer.as_view(), name='cuiquer'),
    url(r'^cookies$', views.Cookies.as_view(), name='cookies'),
    url(r'^condiciones_uso$', views.CondicionesUso.as_view(), name='condiciones_uso'),
    url(r'^condiciones_privacidad$', views.CondicionesPrivacidad.as_view(), name='condiciones_privacidad'),
]
