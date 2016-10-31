from django.views.generic import TemplateView
from landing.forms import ContactoForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from correos.emails import correo_mensaje_agradecimiento, correo_alta_newsletter


class IndexView(TemplateView):
    template_name = 'landing/index.html'


class ComoFuncionaProfesionales(TemplateView):
    template_name = 'landing/como-funciona-profesionales.html'


class ComoFuncionaClientes(TemplateView):
    template_name = 'landing/como-funciona-clientes.html'


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
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()
            correo_mensaje_agradecimiento(contacto.email)
            return HttpResponseRedirect('/')
    else:
        form = ContactoForm()
    return render(request, 'landing/contacto.html', {'form': form})


def validarEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def suscripcion(request):
    from landing.models import Suscripcion
    emails = [m.email for m in Suscripcion.objects.all()]

    if request.method == 'POST':
        email = request.POST.get('email', '')
        nulo = email is None or email is ''

        if not nulo and validarEmail(email) and email not in emails:
            Suscripcion.objects.create(email=email)
            correo_alta_newsletter(email)
            return JsonResponse({'response': True})

    return JsonResponse({'response': False})
