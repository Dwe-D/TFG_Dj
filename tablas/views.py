from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import base64
from .models import sensores

# Create your views here.
def tabla(request):

    return render(request, "tablas/tabla.html")

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        try:
            # Parsear el JSON de la solicitud
            data = json.loads(request.body)
            print("json: ", data)
            # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
            numero1 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero1')
            numero2 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero2')
            numero3 = data.get('uplink_message', {}).get('decoded_payload', {}).get('numero3')
            bolea = data.get('uplink_message', {}).get('decoded_payload', {}).get('bolea')
            erbolean = True if bolea == 1 else False
            print("num1: ", numero1)
            print("num2: ", numero2)
            print("num3: ", numero3)
            print("bolea: ", bolea)

            # Guardar en la base de datos
            mi_modelo = sensores(numero1=numero1, numero2=numero2, numero3=numero3, bolea=erbolean)
            mi_modelo.save()

            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al procesar la solicitud: {str(e)}'}, status=500)
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)


