from django.conf.urls import url
from profesionales.views import ProfesionalCreateView
from profesionales.views import ProfesionalDetailView


urlpatterns = [
    url(r'alta/$', ProfesionalCreateView.as_view(), name='profesional-create'),
    url(r'^(?P<profesional_id>[0-9]+)/$', ProfesionalDetailView.as_view(), name='profesional-detail'),
]
