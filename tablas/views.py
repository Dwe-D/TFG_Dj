from django.shortcuts import render

# Create your views here.

def tabla(request):

    return render(request, "tablas/tabla.html")