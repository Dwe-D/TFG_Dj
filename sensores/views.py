# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import RegistroDispositivoForm
from .models import UsuarioDispositivo, Datos



@csrf_exempt
def deco(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            data = json.loads(request.body)
            # Acceder a los valores del json
            temp = data.get('uplink_message', {}).get('decoded_payload', {}).get('temp')
            hum = data.get('uplink_message', {}).get('decoded_payload', {}).get('hum')
            ppm = data.get('uplink_message', {}).get('decoded_payload', {}).get('ppm')
            lemo_raw = data.get('uplink_message', {}).get('decoded_payload', {}).get('lemo')
            json_eui = data.get('end_device_ids', {}).get('device_id')
            
            eui = UsuarioDispositivo.objects.get(dispositivo_id=json_eui)
            
            #Comprobar
            print("Temp:", temp)
            print("Hum:", hum)
            print("ppm:", ppm)
            print("lemo:", lemo_raw)
            print("EUI:", json_eui)

            lemo=False 
            if lemo_raw == 1:
                lemo=True
            
            #Introducir en la base de datos
            deco = Datos(dispositivo=eui, temp=temp, hum=hum, ppm=ppm, lemo=lemo)
            deco.save()
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
            if UsuarioDispositivo.objects.filter(dispositivo_id=dispositivo_id).exists():
                form.add_error('dispositivo_id', 'Este dispositivo ya está registrado.')
            else:
                # Crear el objeto UsuarioDispositivo si el dispositivo_id es único
                usuario_arduino = form.save(commit=False)
                usuario_arduino.usuario = request.user
                usuario_arduino.save()
                return redirect('Home')  # Redirigir a una página de éxito o a donde prefieras
    else:
        form = RegistroDispositivoForm()

    return render(request, 'dispositivo/registro_dispositivo.html', {'form': form})    

def listar_dispositivos(request):
    dispositivos = UsuarioDispositivo.objects.filter(usuario=request.user)
    return render(request, 'dispositivo/eliminar_dispositivo.html', {'dispositivos': dispositivos})

def eliminar_dispositivos(request):
    if request.method == 'POST':
        dispositivos_a_eliminar = request.POST.getlist('dispositivos_a_eliminar')
        UsuarioDispositivo.objects.filter(id__in=dispositivos_a_eliminar).delete()
        return redirect('elimina')

    return redirect('elimina')

