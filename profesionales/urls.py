from django.conf.urls import url
from profesionales import views


urlpatterns = [
    url(r'alta/$', views.alta_profesional, name='alta-profesional'),
    url(r'actualizar/(?P<codigo_actualizacion>.+)$', views.actualizar_profesional, name='actualizar-profesional'),
]
