from django.shortcuts import render
from django.shortcuts import redirect,render
from vistaymodelo.models import Partidos,Equipo,Estadio,Posiciones
from datetime import date,datetime,timedelta
# Simulando los partidos de la fase de grupos
from itertools import combinations
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
    conteoEquipos = lista_equipo.count() - 1
    if lista_partido:
        return render(request,"enfrentamientos.html",{"listaequipo":lista_equipo,"listapartido":lista_partido})
    else:
        fecha_parti = 0
        mensajes = ""
        for fechas in range(conteoEquipos):
            validacion = 0
            fecha_parti = fecha_parti + 1
            if fecha_parti > 1:
                for equipo1 in lista_equipo:
                    for equipo2 in lista_equipo:
                        if equipo1.nombre != equipo2.nombre:
                                partido_registrar = Partidos(fecha_partido="2020-08-28",local=equipo1.nombre,visitante=equipo2.nombre, resultado_local=equipos.estadio.nombre, fecha=fecha_parti) 
                                
            else:
                for equipos in lista_equipo:
                    if validacion == 0:
                        validacion = 1
                        partido_registrar = Partidos(fecha_partido="2020-08-25",local=equipos.nombre,estadio_jugaran=equipos.estadio.nombre, fecha=fecha_parti) 
                        partido_registrar.save()
                    else: 
                        partid = Partidos.objects.last()
                        if partid:
                            validacion = 0
                            registrarvisitante = Partidos.objects.get(id = partid.id)
                            registrarvisitante.visitante = equipos.nombre
                            registrarvisitante.save()      
               
        return render(request,"enfrentamientos.html",{"listaequipo":lista_equipo,"listapartido":lista_partido,"conteoequipo":conteEquip,"mensaje":mensajes})

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
            po = Posiciones.objects.get(equipo=elocal.nombre)
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
                equipvisitante = Equipo.objects.get(nombre=p.visitante)
                posic_visitante = Posiciones.objects.get(equipo=equipvisitante.id)
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
