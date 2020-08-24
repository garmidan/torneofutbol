from django.shortcuts import render
from django.shortcuts import redirect,render
from vistasymodelos.models import Partidos,Equipo,Estadio
from datetime import date,datetime,timedelta


# Creacion de vistas

#Calendario
def posiciones(request):
    return render(request,"posiciones.html")

def enfrentamientos(request):
    lista_equipo = Equipo.objects.all
    lista_partido = Partidos.objects.all
    return render(request,"enfrentamientos.html",{"listaequipo":lista_equipo,"listapartido":lista_partido})

def registropartidos(request):
    mensaje = 0
    lista_equipo = Equipo.objects.all
    lista_partido = Partidos.objects.all
    if request.method == 'POST':
        equipo_local = request.POST["equipolocal"]
        equipo_visitante = request.POST["equipovisitante"]
        fecha_partido_dia = request.POST["fechapartido"]
        fecha = datetime.now().date()
        if equipo_local == equipo_visitante:
            mensaje = 1
            return render(request, "enfrentamientos.html", {"listaequipo":lista_equipo,"listapartido":lista_partido,"mensaje":mensaje})
        else:
            if str(fecha_partido_dia) < str(fecha):
                mensaje = 2
                return render(request, "enfrentamientos.html", {"listaequipo":lista_equipo,"listapartido":lista_partido,"mensaje":mensaje})
            else:
                estadio_jugar = Equipo.objects.filter(nombre=equipo_local)
                estadio_final = ""
                for dato in estadio_jugar:
                    estadio_final = dato.estadio.nombre
                registrar_partidos = Partidos(fecha_partido=fecha_partido_dia,visitante=equipo_visitante,local=equipo_local,estadio_jugaran=estadio_final)
                registrar_partidos.save()
                return render(request, "enfrentamientos.html", {"listaequipo":lista_equipo,"listapartido":lista_partido})
    else:
        mensaje = "Hubo un error"
    return render(request, "enfrentamientos.html", {"mensaje":mensaje,"listaequipo":lista_equipo,"listapartido":lista_partido})

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
        p.save()
        for partido in lista_partido:
            if str(partido.fecha_partido) < str(fecha):
                lista_final.append(partido)
    return render(request,"agregarResultados.html",{"listapartido":lista_final})
        

