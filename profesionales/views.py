from profesionales.forms import ProfesionalForm
from django.shortcuts import render
from profesionales.models import Servicio
from correos.emails import correos_alta_profesional


def alta_profesional(request):
    servicios = Servicio.objects.all()
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        if form.is_valid():
            profesional = form.save()
            correos_alta_profesional(profesional.usuario.email)
            return render(request, 'profesionales/alta-profesional-finalizada.html', {'profesional': profesional})
    else:
        form = ProfesionalForm()

    return render(request, 'profesionales/profesional-form.html', {'form': form, 'servicios': servicios})
