from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from user.models import Aluno


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('votacao:index'))
    return render(request, template_name='user/login.html')


@require_http_methods(['GET', 'POST'])
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not is_aluno(username):
            return render(request, 'user/login.html', {'error_message': "Utilizador não encontrado"})

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'user/login.html', {'error_message': "Password errada"})

        login(request, user)
        return HttpResponseRedirect(reverse('votacao:index'))

    return render(request, 'user/login.html')


def logoutview(request):
    logout(request)
    return render(request, 'user/login.html')


@require_http_methods(['GET', 'POST'])
def registerview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('votacao:index'))

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        curso = request.POST['curso']
        if Aluno.objects.filter(username=username).exists():
            return render(request, 'user/login.html', {'error_message': "Utilizador já existe"})

        Aluno.objects.create_user(username=username, email=email, password=password, curso=curso)
        return loginview(request)

    return render(request, 'user/register.html')


def is_aluno(username: str) -> bool:
    return Aluno.objects.filter(username=username).exists()
