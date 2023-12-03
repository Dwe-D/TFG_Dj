from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import NumerosModel

# Create your views here.
def tabla(request):

    return render(request, "tablas/tabla.html")

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        # Parsear el JSON de la solicitud
        data = json.loads(request.body)

        # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
        decoded_payload = data.get('data', {}).get('uplink_message', {}).get('decoded_payload', {})
        numero1 = decoded_payload.get('numero1', 0)  # Establecer un valor predeterminado de 0 si 'numero1' no está presente
        numero2 = decoded_payload.get('numero2', 0)  # Establecer un valor predeterminado de 0 si 'numero2' no está presente

        # Guardar en la base de datos
        try:
            mi_modelo = NumerosModel(numero1=numero1, numero2=numero2)
            mi_modelo.save()
            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al guardar en la base de datos: {str(e)}'}, status=500)

    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)