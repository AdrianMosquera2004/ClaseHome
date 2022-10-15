from django.shortcuts import render

# Create your views here.

#Todas las vistas son funciones en PYTHON 

def Home(request):
    return render(request,'home.html')

