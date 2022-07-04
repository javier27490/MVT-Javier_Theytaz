from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from mi_app.models import Curso, Familia
# Create your views here.

def saludo(request):

    fecha_hora_ahora = datetime.now()
    return HttpResponse(f"hola mundo {fecha_hora_ahora} ")

def saludar_a(request, nombre):
    return HttpResponse(f'hola como estas  {nombre.capitalize()}')

def saludo_personalizado(request):
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]

    return render(request, "mi_app/index.html", context )

def listar_cursos(request):
    
    context = {}

    context["cursos"] = Curso.objects.all()

    return render(request, "mi_app/lista_cursos.html", context)

def listar_familia(request):
    
    context = {}

    context["familiares"] = Familia.objects.all()

    return render(request, "mi_app/listar_familia.html", context)


    


