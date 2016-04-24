from django.shortcuts import render
from .models import Projecto
from time import timezone

def lista_de_projs(request):
    post = Projecto.objects.order_by('-votos')
    return render(request,'projs/lista_de_projs.html',{'post' : post})

