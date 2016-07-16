from django.views.generic.edit import CreateView, UpdateView
from profesionales.models import Profesional
from profesionales.forms import ProfesionalForm


class ProfesionalCreate(CreateView):
    model = Profesional
    form_class = ProfesionalForm


class ProfesionalUpdate(UpdateView):
    model = Profesional
    fields = ['name']
