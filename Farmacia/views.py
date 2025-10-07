from datetime import datetime
from operator import truediv
from Farmacia.forms import PostForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from Farmacia import models
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from Farmacia.models import Post

# Create your views here.
def inicio(req):
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(req, 'inicio.html', {
        'variavel': lista
    })


def verDataHora(req):
    agora = datetime.now()
    return render(req, 'data-hora.html', {
        'datahora_atual': agora
    })


def controle(req):
    return render(req, 'controle.html', {
        'variavel': range(10)
    })


@login_required(login_url="/contas/login/")
def postar(req: HttpRequest):
    if req.method == "POST":
        form = PostForm(req.POST, req.FILES)
        if form.is_valid():
            form:Post = form.save(commit = False)
            form.autor = req.user
            if req.user.is_staff:
                form.aprovado = True
            form.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(req, "postar.html", {"formulario": form}) 


def ver_postagens(req):
    todos_posts = models.Post.objects.filter(aprovado=True)
    return render(req, 'listar_posts.html', {
        'postagens': todos_posts
    })

    
def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend=backend.BaseBackend)
            return redirect('home')  # Redireciona para a página inicial após cadastro
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})