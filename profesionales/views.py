from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

from profesionales.models import Profesional
from profesionales.forms import ProfesionalForm


class ProfesionalCreate(CreateView):
    model = Profesional
    form_class = ProfesionalForm
    success_url = reverse_lazy('alta_profesional_finalizada')


class ProfesionalCreateFinished(TemplateView):
    template_name = 'profesionales/alta_finalizada.html'


class ProfesionalUpdate(UpdateView):
    model = Profesional
    fields = ['name']
