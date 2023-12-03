from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NumerosModel
# Create your views here.
#@csrf_exempt
def tabla(request):

    return render(request, "tablas/tabla.html")

def procesar_datos_ttn(request):
    data = request.body.decode("utf-8")
    payload = json.loads(data)
    numero1 = payload["data"]["uplink_message"]["decoded_payload"]["numero1"]
    numero2 = payload["data"]["uplink_message"]["decoded_payload"]["numero2"]

    # Crear una instancia del modelo y guardar en la base de datos
    numeros = NumerosModel(numero1=numero1, numero2=numero2)
    numeros.save()
    return HttpResponse()
        