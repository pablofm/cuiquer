from clientes.forms import ClienteForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


def alta_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente-form.html', {'form': form})
