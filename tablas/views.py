from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import NumerosModel

# Create your views here.
def tabla(request):

    return render(request, "tablas/tabla.html")

@csrf_exempt
@require_POST
def webhook(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Procesa los datos entrantes aquí
        # Extraer los datos que necesitas
        numero1 = data.get('numero1')
        numero2 = data.get('numero2')
        numeros = NumerosModel(numero1=numero1, numero2=numero2)
        numeros.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
