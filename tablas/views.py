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
        nuemro1 = data.get('nuemro1')
        numero2 = data.get('numero2')

        # Guardar en la base de datos
        # Suponiendo que tienes un modelo llamado "MiModelo" con campos "campo1" y "campo2"
        mi_modelo = NumerosModel(numero1=nuemro1, numero=numero2)
        mi_modelo.save()

        return JsonResponse({'mensaje': 'Datos guardados correctamente'})
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)