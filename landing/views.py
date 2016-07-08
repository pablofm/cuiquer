from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'landing/index.html'


class Cuiquer(TemplateView):
    template_name = 'landing/cuiquer.html'
