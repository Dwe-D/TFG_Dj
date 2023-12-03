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
    if request.method == 'POST':
        try:
            # Obtener el contenido JSON de la solicitud
            content = json.loads(request.body.decode('utf-8'))

            # Extraer los datos que necesitas
            numero1 = content.get('numero1')
            numero2 = content.get('numero2')

            # Validar que ambos números estén presentes
            if numero1 is not None and numero2 is not None:
                # Crear una instancia del modelo y guardar en la base de datos
                numeros = NumerosModel(numero1=numero1, numero2=numero2)
                numeros.save()

                return HttpResponse("Datos guardados exitosamente.")
            else:
                return HttpResponseBadRequest("Número1 y Número2 son campos obligatorios.")
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Error al decodificar JSON.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error desconocido: {e}")
    else:
        return HttpResponseBadRequest("Se esperaba una solicitud POST.")