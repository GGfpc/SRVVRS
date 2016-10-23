from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import Comentario,Projecto,Empregado,ProjectoForm,EmpregadoForm,UserForm,BlogPost,BlogForm
import datetime

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

import time

def lista_de_projs(request):
    post = Projecto.objects.order_by('-votos')
    return render(request,'projs/lista_de_projs.html',{'post' : post})


def home(request):
        return render(request, 'projs/home.html', {})


def blog(request):
        posts = BlogPost.objects.all
        return render(request, 'projs/blog.html', {'posts' : posts})

def detalheBlog(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request,'projs/detalheBlog.html', {'post' : post})



def logging(request):
    if request.method == 'POST':
            if "logout" in request.POST:
                print("out")
                logout(request)
                print(request.user.is_authenticated())
                return HttpResponseRedirect("/")
            else:
                email = request.POST["email"]
                pwd = request.POST["pwd"]
                user = authenticate(username=email, password=pwd)
                if user:
                    if user.is_active:
                        login(request, user)
                        print(user.is_authenticated())
                        return HttpResponseRedirect("/")
                else:
                    request.session['last_log'] = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
                    return HttpResponseRedirect('/logging')
    else:
        error = (datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds()
        if 'last_log' in request.session:
            error = ((datetime.datetime.now()-datetime.datetime(1970,1,1)).total_seconds() - request.session['last_log'])
        print(error)
        return render(request,'projs/login.html',{'error' : error})


def voto(request, post_id):
    post = Projecto.objects.get(id=post_id)
    post.votos += 1
    post.save()
    list = request.session['votou']
    list.append(post_id)
    request.session['votou'] = list
    print(request.session['votou'])
    return HttpResponseRedirect("/" + post_id + "/detalheProj")


def apagaComment(request, comment_id):
    post = Comentario.objects.get(id=comment_id)

    post.delete()
    return HttpResponseRedirect('/dash')

def apagaBlogPost(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/dash')

def apagaEmpregado(request, empregado_id):
    post = Empregado.objects.get(id=empregado_id)
    post.delete()
    return HttpResponseRedirect('/dash')

def apagaUser(request,user_id):
    post = User.objects.get(id=user_id)
    post.delete()
    return HttpResponseRedirect('/dash')

def apagaProj(request, post_id):
    post = Projecto.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/dash')

def criaProj(request):
    print('chegou')
    form = ProjectoForm(request.POST)
    if form.is_valid():
        form.save()
        print('gravou')
    return HttpResponseRedirect('/dash')

def criaBlogPost(request):
    print('chegou')
    form = BlogForm(request.POST)
    if form.is_valid():
        form.save()
        print('gravou')
    return HttpResponseRedirect('/dash')

def criaEmpregado(request):
    print('chegou')
    form = ProjectoForm(request.POST)
    if form.is_valid():
        form.save()
        print('gravou')
    return HttpResponseRedirect('/dash')

def criaUser(request):
    print('chegou')
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        print('gravou')
    return HttpResponseRedirect('/dash')



def dashboard(request):

    if request.user.is_authenticated():
        comments = Comentario.objects.all
        users = User.objects.all
        blogposts = BlogPost.objects.all
        empregados = Empregado.objects.all
        projs = Projecto.objects.all
        projform = ProjectoForm
        empregadoform = EmpregadoForm
        userform = UserForm
        blogform = BlogForm

        print(comments)
        return render(request,'projs/dash.html', {'users': users,'comments' : comments, 'empregados' : empregados,
                                                    'projs' : projs, 'projform' : projform,'empregadoform' : empregadoform,
                                                    'userform':userform, 'blogposts' : blogposts, 'blogform' : blogform})
    else:
        return HttpResponseRedirect("/logging")


def comentario(request, post_id):
    session = request.session

    texto = request.POST['comment']

    if("nome" not in session):
        nome = request.POST['name']
        session["nome"] = nome
    session["nrcomments"] += 1
    post = post = Projecto.objects.get(id=post_id)
    comment = Comentario(texto=texto, autor=session["nome"], proj=post)
    comment.save()
    return HttpResponseRedirect("/" + post_id + "/detalheProj")

def detalheProj(request, post_id):
    if 'votou' not in request.session:
        request.session['votou'] = []
    if 'nrcomments' not in request.session:
        request.session['nrcomments'] = 0
    post = Projecto.objects.get(id=post_id)
    lista = Comentario.objects.filter(proj=post)
    return render(request,'projs/detalheProj.html', {'lista' : lista, 'post' : post})


