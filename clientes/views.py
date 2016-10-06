from clientes.forms import ClienteForm
from django.shortcuts import render
from profesionales.models import Servicio


def alta_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'clientes/alta-cliente-finalizada.html')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente-form.html', {'form': form})
