from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.inicio, name='home'),
    path('data-hora/', views.verDataHora, name='agora'),
    path('controle/', views.controle, name='lista'),
    path('postar/', views.postar, name='postar'),
    path('Postagens/', views.ver_postagens, name='listaposts'),
    path('registrar/', views.registrar, name='registrar'),
    path('contas/', include("django.contrib.auth.urls")),
]