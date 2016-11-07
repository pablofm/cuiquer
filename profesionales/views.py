from uuid import UUID
from django.http import Http404

from profesionales.forms import ProfesionalForm, ProfesionalExtraForm
from django.shortcuts import render
from profesionales.models import Servicio, Profesional
from correos.emails import correos_alta_profesional
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


def alta_profesional(request):
    servicios = Servicio.objects.all()
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            profesional = form.save()
            link_relativo = reverse(
                'actualizar-profesional', kwargs={'codigo_actualizacion': profesional.codigo_actualizacion})
            link = request.build_absolute_uri(link_relativo)

            correos_alta_profesional(profesional.usuario.email, link)
            return render(request, 'profesionales/alta-profesional-finalizada.html', {'profesional': profesional})
    else:
        form = ProfesionalForm()

    return render(request, 'profesionales/profesional-form.html', {'form': form, 'servicios': servicios})


def actualizar_profesional(request, codigo_actualizacion):
    try:
        UUID(codigo_actualizacion, version=4)
    except ValueError:
        raise Http404
    servicios = Servicio.objects.all()
    profesional = get_object_or_404(Profesional, codigo_actualizacion=codigo_actualizacion)
    if request.method == 'POST':
        form = ProfesionalExtraForm(request.POST, request.FILES, profesional=profesional)
        if form.is_valid():
            profesional = form.save()
            return render(request, 'profesionales/alta-profesional-finalizada.html', {'profesional': profesional})
    else:
        form = ProfesionalExtraForm(profesional=profesional)

    return render(request, 'profesionales/actualizar-profesional.html', {'form': form, 'servicios': servicios})
