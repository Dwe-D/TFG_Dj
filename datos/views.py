from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from sensores.models import UsuarioDispositivo, Datos
from math import ceil

# Función para obtener la tabla paginada
def paginas(datos_tabla, page, cantidad_por_pagina):
    num_paginas = ceil(len(datos_tabla) / cantidad_por_pagina)
    paginator = Paginator(datos_tabla, cantidad_por_pagina)

    try:
        tabla = paginator.page(page)
    except PageNotAnInteger:
        tabla = paginator.page(1)
    except EmptyPage:
        tabla = paginator.page(paginator.num_pages)

    return tabla, int(page), cantidad_por_pagina, num_paginas

# Vista principal
def No_Fil(request):
    if request.user.is_authenticated:
        cantidad_por_pagina = 25
        datos_tabla = Datos.objects.filter(dispositivo__usuario=request.user).order_by('-fecha_creacion')
        page = request.GET.get('page', 1)

        tabla, page, cantidad_por_pagina, num_paginas = paginas(datos_tabla, page, cantidad_por_pagina)

        context = {
            'tabla': tabla,
            'page': page,
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }
        return render(request, "tablas/tabla.html", context)
    else:
        return redirect('login')

def listar_DF(request):
    dispositivos = UsuarioDispositivo.objects.filter(usuario=request.user)
    return render(request, 'filtros/filtro_dis_dia.html', {'dispositivos': dispositivos})

def tabla_DF(request):
    if request.user.is_authenticated and request.method == 'POST':
        dispositivos_seleccionados = request.POST.getlist('dispositivos_seleccionados')
        fecha_busqueda = request.POST.get('fecha_busqueda')

        datos_filtrados = Datos.objects.filter(
            dispositivo__usuario=request.user,
            dispositivo__id__in=dispositivos_seleccionados,
            fecha_creacion__date=fecha_busqueda
        ).order_by('-fecha_creacion')

        cantidad_por_pagina = 25
        page = request.GET.get('page', 1)

        tabla, page, cantidad_por_pagina, num_paginas = paginas(datos_filtrados, page, cantidad_por_pagina)

        context = {
            'tabla': tabla,
            'page': page,
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }

        return render(request, "tablas/tabla.html", context)
    else:
        return redirect('login')

def listar_F(request):	
    return render(request, "filtros/filtro_fecha.html")

def tabla_F(request):
    if request.user.is_authenticated and request.method == 'POST':
        fecha_busqueda = request.POST.get('fecha_busqueda')

        datos_filtrados = Datos.objects.filter(
            dispositivo__usuario=request.user,
            fecha_creacion__date=fecha_busqueda
        ).order_by('-fecha_creacion')
        
        cantidad_por_pagina = 25
        page = request.GET.get('page', 1)

        tabla, page, cantidad_por_pagina, num_paginas = paginas(datos_filtrados, page, cantidad_por_pagina)

        context = {
            'tabla': tabla,
            'page': page,
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }

        return render(request, "tablas/tabla.html", context)
    else:
        return redirect('login')

def listar_PPM(request):	
    return render(request, "filtros/filtro_ppm.html")

def tabla_PPM(request):
    if request.user.is_authenticated and request.method == 'POST':
        ppm_busqueda = request.POST.get('ppm_busqueda')

        datos_filtrados = Datos.objects.filter(
            dispositivo__usuario=request.user,
            ppm__gte=ppm_busqueda
        ).order_by('-fecha_creacion')

        cantidad_por_pagina = 25
        page = request.GET.get('page', 1)

        tabla, page, cantidad_por_pagina, num_paginas = paginas(datos_filtrados, page, cantidad_por_pagina)

        context = {
            'tabla': tabla,
            'page': page,
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }

        return render(request, "tablas/tabla.html", context)
    else:
        return redirect('login')



def listar_DPPM(request):
    dispositivos = UsuarioDispositivo.objects.filter(usuario=request.user)
    return render(request, 'filtros/filtro_dis_ppm.html', {'dispositivos': dispositivos})

    
def tabla_DPPM(request):
    if request.user.is_authenticated and request.method == 'POST':
        dispositivos_seleccionados = request.POST.get('dispositivos_seleccionados')
        ppm_busqueda = request.POST.get('ppm_busqueda')
        print("Dispositivos seleccionados:", dispositivos_seleccionados)
        print("Fecha de búsqueda:", ppm_busqueda)
		
        datos_filtrados = Datos.objects.filter(
            dispositivo__usuario=request.user,
            dispositivo__id=dispositivos_seleccionados,
            ppm__gte=ppm_busqueda
        ).order_by('-fecha_creacion')

        cantidad_por_pagina = 25
        page = request.GET.get('page', 1)

        tabla, page, cantidad_por_pagina, num_paginas = paginas(datos_filtrados, page, cantidad_por_pagina)

        context = {
            'tabla': tabla,
            'page': page,
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }

        return render(request, "tablas/tabla.html", context)
    else:
        return redirect('login')
    
def listar_D(request):
    dispositivos = UsuarioDispositivo.objects.filter(usuario=request.user)
    return render(request, 'filtros/filtro_dis.html', {'dispositivos': dispositivos})    

def tabla_D(request):
    if request.user.is_authenticated and request.method == 'POST':
        dispositivos_seleccionados = request.POST.get('dispositivos_seleccionados')
		
        datos_filtrados = Datos.objects.filter(
            dispositivo__usuario=request.user,
            dispositivo__id=dispositivos_seleccionados,
        ).order_by('-fecha_creacion')

        cantidad_por_pagina = 25
        page = request.GET.get('page', 1)

        tabla, page, cantidad_por_pagina, num_paginas = paginas(datos_filtrados, page, cantidad_por_pagina)

        context = {
            'tabla': tabla,
            'page': page,
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }

        return render(request, "tablas/tabla.html", context)
    else:
        return redirect('login')
