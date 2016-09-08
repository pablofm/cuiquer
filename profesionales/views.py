from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from profesionales.forms import ProfesionalForm
from profesionales.models import Profesional


class ProfesionalDetailView(DetailView):
    model = Profesional
    form_class = ProfesionalForm
    pk_url_kwarg = 'profesional_id'


class ProfesionalCreateView(CreateView):
    model = Profesional
    form_class = ProfesionalForm
