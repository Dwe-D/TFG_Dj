from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import base64
from .models import NumerosModel

# Create your views here.
def tabla(request):

    return render(request, "tablas/tabla.html")

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            data = json.loads(request.body)
            
            #data = json.loads(json_data)
            

            # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
            numero1 = data.get('data', {}).get('uplink_message', {}).get('decoded_payload', {}).get('numero1')
            numero2 = data.get('data', {}).get('uplink_message', {}).get('decoded_payload', {}).get('numero2')

            # Verificar si los campos son None y establecer valores predeterminados
            numero1 = 0 if numero1 is None else numero1
            numero2 = 0 if numero2 is None else numero2

            # Guardar en la base de datos
            mi_modelo = NumerosModel(numero1=numero1, numero2=numero2)
            mi_modelo.save()

            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)


