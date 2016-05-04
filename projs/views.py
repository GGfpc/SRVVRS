from django.shortcuts import render
from .models import Projecto
from time import timezone
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

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

def voto(request, post_id):

    post = Projecto.objects.get(id=post_id)
    post.votos += 1
    post.save()
    return HttpResponseRedirect("/")


