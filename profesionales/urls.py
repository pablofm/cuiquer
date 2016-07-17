from django.conf.urls import url
from profesionales.views import ProfesionalCreate, ProfesionalUpdate, ProfesionalCreateFinished


urlpatterns = [
    url(r'alta/$', ProfesionalCreate.as_view(), name='alta_profesional'),
    url(r'alta_finalizada/$', ProfesionalCreateFinished.as_view(), name='alta_profesional_finalizada'),
    url(r'(?P<pk>[0-9]+)/$', ProfesionalUpdate.as_view(), name='actualizar_profesional'),
]
