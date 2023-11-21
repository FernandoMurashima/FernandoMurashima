from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Fernando Murashima',
    })

def sobre(request):
    return HttpResponse("uma linda resposta! - SOBRE novo")

def contato(request):
    return HttpResponse("uma linda resposta! - CONTATO novo")   