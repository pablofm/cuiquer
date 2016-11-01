from clientes.forms import ClienteForm
from django.shortcuts import render
from correos.emails import correos_alta_cliente


def alta_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            correos_alta_cliente(cliente.usuario.email)
            return render(request, 'clientes/alta-cliente-finalizada.html')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente-form.html', {'form': form})
