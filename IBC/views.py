


from django.http import HttpResponse
from django.shortcuts import render


def inicio(request):
    return render(request,'index.html')


def formulario(request):
    return render(request,'form.html')

def enfoque(request):
    return render(request,'enfoque.html')


def resultados(request):
    return render(request,'resultados.html')

def ml(request):
    return render(request,'ml.html')