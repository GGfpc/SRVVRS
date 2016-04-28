from django.shortcuts import render
from .models import Projecto
from time import timezone
from django.http import HttpResponseRedirect, HttpResponse

def lista_de_projs(request):
    post = Projecto.objects.order_by('-votos')
    return render(request,'projs/lista_de_projs.html',{'post' : post})

def home(request):
    return render(request, 'projs/home.html', {})


def voto(request, post_id):
    post = Projecto.objects.get(id=post_id)
    post.votos += 1
    post.save()
    return HttpResponseRedirect("/")


