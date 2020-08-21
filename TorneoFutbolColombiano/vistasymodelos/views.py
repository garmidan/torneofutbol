from django.shortcuts import render
from django.shortcuts import redirect,render
from vistasymodelos.models import Partidos,Equipo,Estadio



# Creacion de vistas

#Calendario
def posiciones(request):
    mensaje = "Hola"
    return render(request,"posiciones.html",{"mensaje":mensaje})

def enfrentamientos(request):
    lista_equipo = Equipo.objects.all
    lista_partido = Partidos.objects.all
    return render(request,"enfrentamientos.html",{"listaequipo":lista_equipo,"listapartido":lista_partido})

def registropartidos(request):
    lista_equipo = Equipo.objects.all
    lista_partido = Partidos.objects.all
    if request.method == 'POST':
        equipo_local = request.POST["equipolocal"]
        equipo_visitante = request.POST["equipovisitante"]
        fecha_partido_dia = request.POST["fechapartido"]
        registrar_partidos = Partidos(nombres_equipos=equipo_local+" VS "+equipo_visitante,fecha_partido=fecha_partido_dia,visitante=equipo_visitante,local=equipo_local)
        registrar_partidos.save()
        return render(request, "enfrentamientos.html", {"listaequipo":lista_equipo,"listapartido":lista_partido})
    else:
        mensaje = "Hubo un error"
    return render(request, "enfrentamientos.html", {"mensaje":mensaje,"listaequipo":lista_equipo,"listapartido":lista_partido})

