from django.views.generic.edit import CreateView, UpdateView
from profesionales.models import Profesional


class ProfesionalCreate(CreateView):
    model = Profesional
    fields = '__all__'


class ProfesionalUpdate(UpdateView):
    model = Profesional
    fields = ['name']
