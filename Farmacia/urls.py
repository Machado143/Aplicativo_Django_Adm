from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse



@ensure_csrf_cookie
def get_csrf_token(request):
    csrf_token = request.COOKIES.get('csrftoken', '')
    return JsonResponse({'csrf_token': csrf_token})

urlpatterns = [
    path('', views.inicio, name='home'),
    path('data-hora/', views.verDataHora, name='agora'),
    path('controle/', views.controle, name='lista'),
    path('postar/', views.postar, name='postar'),
    path('Postagens/', views.ver_postagens, name='listaposts'),
    path('registrar/', views.registrar, name='registrar'),
    path('contas/', include("django.contrib.auth.urls")),
    path('api/csrf/', get_csrf_token),
]

