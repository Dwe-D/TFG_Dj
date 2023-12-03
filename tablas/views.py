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
        # Parsear el JSON de la solicitud
        data = json.loads(request.body)

        # Imprimir para debuggeo
        print("Datos completos:", data)

        # Acceder a los valores de numero1 y numero2 dentro de decoded_payload
        uplink_message = data.get('data', {}).get('uplink_message', {})
        decoded_payload = uplink_message.get('decoded_payload', {})
        
        # Imprimir para debuggeo
        print("decoded_payload:", decoded_payload)

        # Acceder a frm_payload y decodificarlo
        frm_payload_base64 = decoded_payload.get('frm_payload', '')
        try:
            frm_payload_bytes = base64.b64decode(frm_payload_base64)
            frm_payload_str = frm_payload_bytes.decode('utf-8')
            frm_payload = json.loads(frm_payload_str)
        except (base64.binascii.Error, json.JSONDecodeError) as e:
            return JsonResponse({'error': f'Error al decodificar el payload: {str(e)}'}, status=400)

        # Imprimir para debuggeo
        print("frm_payload:", frm_payload)

        # Acceder a los valores de numero1 y numero2
        numero1 = frm_payload.get('numero1', 0)
        numero2 = frm_payload.get('numero2', 0)

        # Imprimir para debuggeo
        print("numero1:", numero1)
        print("numero2:", numero2)

        # Guardar en la base de datos
        try:
            mi_modelo = NumerosModel(numero1=numero1, numero2=numero2)
            mi_modelo.save()
            return JsonResponse({'mensaje': 'Datos guardados correctamente'})
        except Exception as e:
            return JsonResponse({'error': f'Error al guardar en la base de datos: {str(e)}'}, status=500)

    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)