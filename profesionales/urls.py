from django.conf.urls import url
from profesionales import views
# from profesionales.views import ProfesionalDetailView


urlpatterns = [
    url(r'alta/$', views.alta_profesional, name='alta-profesional'),
    # url(r'^(?P<profesional_id>[0-9]+)/$', ProfesionalDetailView.as_view(), name='profesional-detail'),
]
