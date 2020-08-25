from django.shortcuts import render
from django.shortcuts import redirect,render
from vistaymodelo.models import Partidos,Equipo,Estadio,Posiciones
from datetime import date,datetime,timedelta
import random

# Creacion de vistas

#Calendario
def posiciones(request):
    lista_posiciones = Posiciones.objects.all().order_by('-puntos')
    return render(request,"posiciones.html",{"listaposiciones":lista_posiciones})

def enfrentamientos(request):
    lista_equipo = Equipo.objects.all()
    lista_partido = Partidos.objects.all()
    conteEquip = lista_equipo.count()
    enfrentamiento_pares = []
    enfrentamiento_impares = []
    conteoEquipos = lista_equipo.count() + 1
    if lista_partido:
        return render(request,"enfrentamientos.html",{"listaequipo":lista_equipo,"listapartido":lista_partido})
    else:
        return render(request,"enfrentamientos.html",{"listaequipo":lista_equipo,"listapartido":lista_partido,"conteoequipo":conteEquip,"pares":enfrentamiento_pares,"impares": enfrentamiento_impares})

def calendario(request):
    lista_partido = Partidos.objects.all()
    lista_final = []
    fecha = datetime.now().date()
    for partido in lista_partido:
        if str(partido.fecha_partido) > str(fecha):
            lista_final.append(partido)
    return render(request,"calendario.html",{"listapartido":lista_final})

def resultados(request):
    lista_partido = Partidos.objects.all()
    lista_final = []
    fecha = datetime.now().date()
    for partido in lista_partido:
        if str(partido.fecha_partido) < str(fecha):
            lista_final.append(partido)
    return render(request,"agregarResultados.html",{"listapartido":lista_final})

def agregarresultados(request):
    lista_equipo = Equipo.objects.all
    lista_partido = Partidos.objects.all
    if request.method == 'POST':
        id_partido = request.POST["id"]
        resultado_partido = Partidos.objects.filter(id = id_partido)
        return render(request, "addResult.html", {"listaequipo":lista_equipo,"listapartido":lista_partido,"addresultado":resultado_partido})
    return render(request, "agregarResultados.html", {"listaequipo":lista_equipo,"listapartido":lista_partido})

def agregarresultadofinal(request):
    lista_partido = Partidos.objects.all()
    lista_final = []
    fecha = datetime.now().date()
    if request.method == 'POST':
        id_resultado = request.POST["idedit"]
        p = Partidos.objects.get(id=id_resultado)
        p.resultado_local = request.POST['resultlocal']
        p.resultado_visitante = request.POST['resultvisitante']
        if request.POST['resultlocal'] > request.POST['resultvisitante']:
            elocal = Equipo.objects.get(nombre=p.local)
            po = Posiciones.objects.get(equipo=elocal)
            if po:
                po.puntos = po.puntos + 3
                po.save()
            else:
                pos = Posiciones(puntos= 3, equipo=p.local)
                pos.save()
        else:
            if request.POST['resultlocal'] == request.POST['resultvisitante']:
                polocal = Posiciones.objects.get(equipo=p.local)
                povisitante = Posiciones.objects.get(equipo=p.visitante)
                if polocal:
                    polocal.puntos = polocal.puntos + 1
                    polocal.save()
                else:
                    polocal = Posiciones(puntos= 1, equipo=p.local)
                    polocal.save()
                if povisitante:
                    povisitante.puntos = polocal.puntos + 1
                    povisitante.save()
                else:
                    polocal = Posiciones(puntos= 1, equipo=p.visitante)
                    polocal.save()
            else:
                posic_visitante = Posiciones.objects.get(equipo=p.visitante)
                if posic_visitante:
                    posic_visitante.puntos = polocal.puntos + 3
                    posic_visitante.save()
                else:
                    posic_visitante = Posiciones(puntos= 3, equipo=p.visitante)
                    posic_visitante.save()
        p.save()
        for partido in lista_partido:
            if str(partido.fecha_partido) < str(fecha):
                lista_final.append(partido)
    return render(request,"agregarResultados.html",{"listapartido":lista_final})
