from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'landing/index.html'


class Cuiquer(TemplateView):
    template_name = 'landing/cuiquer.html'


class CondicionesUso(TemplateView):
    template_name = 'landing/condiciones_uso.html'


class CondicionesPrivacidad(TemplateView):
    template_name = 'landing/condiciones_privacidad.html'


class Cookies(TemplateView):
    template_name = 'landing/cookies.html'
