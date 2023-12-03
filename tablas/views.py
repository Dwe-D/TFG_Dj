from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from .models import NumerosModel
# Create your views here.
@csrf_exempt
def tabla(request):

    return render(request, "tablas/tabla.html")

def procesar_datos_ttn(request):
    try:
        data = request.body.decode("utf-8")
        payload = json.loads(data)

        # Validate the decoded data
        print(json.dumps(payload, indent=4))  # Print the decoded payload for inspection

        numero1 = payload["data"]["uplink_message"]["decoded_payload"]["numero1"]
        numero2 = payload["data"]["uplink_message"]["decoded_payload"]["numero2"]

        # Create a new instance of the NumerosModel and save it to the database
        numeros = NumerosModel(numero1=numero1, numero2=numero2)
        numeros.save()

        return HttpResponse()
    except Exception as e:
        # Handle any exceptions that occur during data processing
        print(f"Error processing JSON data: {e}")
        return HttpResponseBadRequest()