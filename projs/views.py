from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Projecto, Comentario
from time import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
import time

def lista_de_projs(request):

    post = Projecto.objects.order_by('-votos')
    return render(request,'projs/lista_de_projs.html',{'post' : post})


def home(request):
        return render(request, 'projs/home.html', {})


def logging(request):
    print("coiso")
    if request.method == 'POST':
            if "logout" in request.POST:
                print("out")
                logout(request)
                print(request.user.is_authenticated())
                return HttpResponseRedirect("/home")
            else:
                email = request.POST["email"]
                pwd = request.POST["pwd"]
                user = authenticate(username=email, password=pwd)
                if user:
                    if user.is_active:
                        login(request, user)
                        print(user.is_authenticated())
                        return HttpResponseRedirect("/home")
                else:
                    return render(request,'projs/login.html',{})


def voto(request, post_id):
    post = Projecto.objects.get(id=post_id)
    post.votos += 1
    post.save()
    return HttpResponseRedirect("/")


def comentario(request, post_id):
    session = request.session

    texto = request.POST['comment']


    if("nome" not in session):
        nome = request.POST['name']
        session["nome"] = nome

    if("nrcomments" not in session):
        session["nrcomments"] = 1
    else:
        session["nrcomments"] += 1

    if(session["nrcomments"] <= 3):
        post = post = Projecto.objects.get(id=post_id)
        comment = Comentario(texto=texto, autor=session["nome"], proj=post)
        comment.save()
    else:
        return HttpResponse("Já comentou demasiado")


    return HttpResponseRedirect("/")

def detalheProj(request, post_id):

    post = Projecto.objects.get(id=post_id)
    lista = Comentario.objects.filter(proj=post)
    print(lista)

    return render(request,'projs/detalheProj.html', {'lista' : lista, 'post' : post})


