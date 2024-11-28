from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def educacion(request):
    return render(request, 'educacion.html')

def habilidades(request):
    return render(request, 'habilidades.html')

def proyectos(request):
    return render(request, 'proyectos.html')
