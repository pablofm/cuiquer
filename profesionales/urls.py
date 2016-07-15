from django.conf.urls import url
from profesionales.views import ProfesionalCreate, ProfesionalUpdate


urlpatterns = [
    url(r'add/$', ProfesionalCreate.as_view(), name='anadir_profesional'),
    url(r'(?P<pk>[0-9]+)/$', ProfesionalUpdate.as_view(), name='actualizar_profesional'),
]
