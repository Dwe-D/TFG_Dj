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
        data = request.POST
        numero1 = data.get('numero1')
        numero2 = data.get('numero2')
        NumerosModel.objects.create(numero1=numero1, numero2=numero2)
        return JsonResponse({'status': 'success'}, status=200)
    else:
        return JsonResponse({'status': 'failed', 'error': 'Not a POST request'}, status=400)