# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import base64
from bd_masfilas.models import teclado
from math import ceil
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import RegistroDispositivoForm
from .models import UsuarioArduino, DatosDispositivo

# Create your views here.
def tabla(request):
    if request.user.is_authenticated:
        cantidad_por_pagina = 25
        page = request.GET.get('page', 1)

        # Filtra los DatosDispositivo asociados al usuario actual y ordena por fecha de creación descendente
        datos_tabla = DatosDispositivo.objects.filter(dispositivo__usuario=request.user).order_by('-fecha_creacion')

        # Calcular el número máximo de páginas
        num_paginas = ceil(len(datos_tabla) / cantidad_por_pagina)

        # Usar Paginator para obtener la porción de datos para la página actual
        paginator = Paginator(datos_tabla, cantidad_por_pagina)
        try:
            datos_teclado = paginator.page(page)
        except PageNotAnInteger:
            datos_teclado = paginator.page(1)
        except EmptyPage:
            datos_teclado = paginator.page(paginator.num_pages)

        # Pasa los datos al template
        context = {
            'datos_teclado': datos_teclado,
            'page': int(page),
            'cantidad_por_pagina': cantidad_por_pagina,
            'num_paginas': num_paginas,
        }
        return render(request, "tablas/tabla_test.html", context)
    else:
        return redirect('login')

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            data = json.loads(request.body)
            # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
            numero1 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero1')
            numero2 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero2')
            numero3 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero3')
            numeroB = data.get('uplink_message', {}).get('decoded_payload', {}).get('numeroB')
            eui = data.get('end_device_ids', {}).get('device_id')
            print("n1:", numero1)
            print("n2:", numero2)
            print("n3:", numero3)
            print("nB:", numeroB)
            print("EUI:", eui)

            boolean=False 
            # Verificar si los campos son None y establecer valores predeterminados
            if numeroB == 1:
                boolean=True

            
            raton = teclado(numero1=numero1, numero2=numero2, numero3=numero3, numeroB=numeroB)
            raton.save()
            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)

def reg(request):
    if request.method == 'POST':
        form = RegistroDispositivoForm(request.POST)
        if form.is_valid():
            dispositivo_id = form.cleaned_data['dispositivo_id']

            # Verificar si el dispositivo_id ya existe
            if UsuarioArduino.objects.filter(dispositivo_id=dispositivo_id).exists():
                form.add_error('dispositivo_id', 'Este dispositivo ya está registrado.')
            else:
                # Crear el objeto UsuarioArduino si el dispositivo_id es único
                usuario_arduino = form.save(commit=False)
                usuario_arduino.usuario = request.user
                usuario_arduino.save()
                return redirect('Home')  # Redirigir a una página de éxito o a donde prefieras
    else:
        form = RegistroDispositivoForm()

    return render(request, 'registro_dispositivo/registro_dispositivo.html', {'form': form})

def meter(request):
    eui12 = UsuarioArduino.objects.get(dispositivo_id='eui-a8610a3130467612')  # Reemplaza 'dispositivo_existente' con el dispositivo_id real
    eui13 = UsuarioArduino.objects.get(dispositivo_id='eui-a8610a3130467613')  # Reemplaza 'dispositivo_existente' con el dispositivo_id real

    temp=10.2
    temp1=33.2
    hum=77.3
    hum1=12.123

    for i in range(67):
        test=DatosDispositivo(dispositivo=eui13, temp=temp, hum=hum)
        test.save()
    for i in range(30):
        test1=DatosDispositivo(dispositivo=eui12, temp=temp1, hum=hum1)
        test1.save()
    return HttpResponse


@csrf_exempt
def deco(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            data = json.loads(request.body)
            # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
            temp = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero1')
            hum = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero2')
            numero3 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero3')
            numeroB = data.get('uplink_message', {}).get('decoded_payload', {}).get('numeroB')
            json_eui = data.get('end_device_ids', {}).get('device_id')
            eui = UsuarioArduino.objects.get(dispositivo_id=json_eui)

            print("n1:", temp)
            print("n2:", hum)
            print("n3:", numero3)
            print("nB:", numeroB)
            print("EUI:", json_eui)
            boolean=False 
            # Verificar si los campos son None y establecer valores predeterminados
            if numeroB == 1:
                boolean=True
            
            deco = DatosDispositivo(dispositivo=eui, temp=temp, hum=hum)
            deco.save()
            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)