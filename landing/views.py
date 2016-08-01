from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from landing.forms import ContactoForm
from django.core.urlresolvers import reverse_lazy


class Index(TemplateView):
    template_name = 'landing/index.html'


class Cuiquer(CreateView):
    template_name = 'landing/cuiquer.html'
    form_class = ContactoForm
    success_url = reverse_lazy('index')


class CondicionesUso(TemplateView):
    template_name = 'landing/condiciones_uso.html'


class CondicionesPrivacidad(TemplateView):
    template_name = 'landing/condiciones_privacidad.html'


class Cookies(TemplateView):
    template_name = 'landing/cookies.html'
