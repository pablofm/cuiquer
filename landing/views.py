from django.views.generic import TemplateView
from landing.forms import ContactoForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse


class IndexView(TemplateView):
    template_name = 'landing/index.html'


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


def contacto(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactoForm()
    return render(request, 'landing/contacto.html', {'form': form})


def suscripcion(request):
    from landing.models import Suscripcion
    emails = [m.email for m in Suscripcion.objects.all()]

    if request.method == 'POST':
        email = request.POST.get('email', None)
        print(emails)
        print(email)
        print(email in emails)
        if email is not None and email not in emails:
            Suscripcion.objects.create(email=email)
            return JsonResponse({'response': True})

    return JsonResponse({'response': False})
