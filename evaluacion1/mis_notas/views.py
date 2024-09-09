from django.shortcuts import render
from .models import Notas, Nota

n = Notas()

# Create your views here.
def index(request):
    return render(request, 'mis_notas/base.html')

def home(request):
    return render(request, 'mis_notas/home.html', {'mensaje':'Bienvenido'})

# ----------------------------------------------------------------------------- #

def notas(request):
    return render(request, 'mis_notas/notas.html', {'notas': n.listar_notas()})

def eliminar(request):
    titulo = request.POST.get('title')
    
    if titulo != '':
        mensaje = n.eliminar_nota(titulo)
    return render(request, 'mis_notas/eliminar.html', {'mensaje':mensaje})

def crear(request):
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    importante = request.POST.get('importante')

    if titulo != '' or descripcion != '':
        nuevanota = Nota(titulo, descripcion, bool(importante))
        mensaje = n.crear_notas(nuevanota)
    else:
        mensaje = 'Campos vacios'

    return render(request, 'mis_notas/crear.html', {'mensaje':mensaje})