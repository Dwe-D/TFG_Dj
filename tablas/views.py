from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import base64
from bd.models import sensores
from bd_masfilas.models import teclado

# Create your views here.
def tabla(request):

    return render(request, "tablas/tabla.html")

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            data = json.loads(request.body)
            print("json:", data)
            # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
            numero1 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero1')
            numero2 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero2')
            numero3 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero3')
            numeroB = data.get('uplink_message', {}).get('decoded_payload', {}).get('numeroB')
            print("n1:", numero1)
            print("n2:", numero2)
            print("n3:", numero3)
            print("nB:", numeroB)
            boolean=False 
            # Verificar si los campos son None y establecer valores predeterminados
            if numeroB == 1:
                boolean=True

            # Guardar en la base de datos
            mi_modelo = sensores(numero1=numero1, numero2=numero2)
            mi_modelo.save()
            raton = teclado(numero1=numero1, numero2=numero2, numero3=numero3, numeroB=numeroB)
            raton.save()
            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)

