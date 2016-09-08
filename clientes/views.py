from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from clientes.models import Cliente
from clientes.forms import ClienteForm


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm


class ClienteDetailView(DetailView):
    model = Cliente
    form_class = ClienteForm
    pk_url_kwarg = 'cliente_id'
