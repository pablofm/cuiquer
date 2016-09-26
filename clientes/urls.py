from django.conf.urls import url
from clientes import views


urlpatterns = [
    url(r'alta/$', views.alta_cliente, name='alta-cliente'),
]
