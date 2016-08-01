from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from landing.forms import ContactoForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
from landing.models import NewsLetter


def index(request):
    return render(request, 'landing/index.html')


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


class CondicionesUso(TemplateView):
    template_name = 'landing/condiciones_uso.html'


class CondicionesPrivacidad(TemplateView):
    template_name = 'landing/condiciones_privacidad.html'


class Cookies(TemplateView):
    template_name = 'landing/cookies.html'
