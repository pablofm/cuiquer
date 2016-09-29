from profesionales.forms import ProfesionalForm
from django.shortcuts import render
from django.http import HttpResponseRedirect


def alta_profesional(request):
    if request.method == 'POST':
        form = ProfesionalForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print("caca")
            print("Form errors: {}".format(form))
    else:
        form = ProfesionalForm()

    return render(request, 'profesionales/profesional-form.html', {'form': form})
