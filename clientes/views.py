from django.views.generic.edit import CreateView  # , UpdateView
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

from clientes.models import Cliente
from clientes.forms import ClienteForm


class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = reverse_lazy('alta_cliente_finalizada')


class ClienteCreateFinished(TemplateView):
    template_name = 'clientes/alta_finalizada.html'


# class ClienteUpdate(UpdateView):
#     model = Cliente
#     fields = '__all__'
