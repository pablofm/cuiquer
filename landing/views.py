from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from landing.forms import ContactoForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
from landing.models import NewsLetter


class IndexView(TemplateView):
    template_name = 'landing/index.html'


def newsletter(request):
    if request.method == 'POST':
        email = request.POST['email']
        very_exist = [m.email for m in NewsLetter.objects.all()]
        if email in very_exist:
            msg = "Su email ya está apuntado al newsletter."
            return JsonResponse({'msg': msg})

        NewsLetter.objects.create(email=email)
        msg = "Hemos apuntado su email al newsletter."
        return JsonResponse({'msg': msg})


class Cuiquer(CreateView):
    template_name = 'landing/cuiquer.html'
    form_class = ContactoForm
    success_url = reverse_lazy('index')


class Servicios(TemplateView):
    template_name = 'landing/secundarias/todos-nuestros-serviciosservicios_ofrecidos.html'


class ComoFunciona(TemplateView):
    template_name = 'landing/profesionales-como.html'


# Secundarias
class SaludYBienestarView(TemplateView):
    template_name = 'landing/secundarias/salud-y-bienestar.html'


class CuidadoDePersonasView(TemplateView):
    template_name = 'landing/secundarias/cuidado-de-personas.html'


class ClasesParticulares(TemplateView):
    template_name = 'landing/secundarias/clases-particulares.html'


class MonitorDeDeportesView(TemplateView):
    template_name = 'landing/secundarias/monitor-de-deportes.html'


class HogarYLimpiezaView(TemplateView):
    template_name = 'landing/secundarias/hogar-y-limpieza.html'


class ServiciosInformaticosView(TemplateView):
    template_name = 'landing/secundarias/servicios-informaticos.html'


class ReparacionesYReformasView(TemplateView):
    template_name = 'landing/secundarias/reparaciones-y-reformas.html'


class TodosNuestrosServiciosView(TemplateView):
    template_name = 'landing/secundarias/todos-nuestros-servicios.html'


# Legal
class CondicionesUsoView(TemplateView):
    template_name = 'landing/legal/condiciones-uso.html'


class CondicionesPrivacidadView(TemplateView):
    template_name = 'landing/legal/condiciones-privacidad.html'


class CookiesView(TemplateView):
    template_name = 'landing/legal/cookies.html'
