from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('votacao:index'))
    return render(request, template_name='user/home.html')


def loginview(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('votacao:index'))
    else:
        return render(request, 'user/home.html', {'error_message': "Utilizador não encontrado"})


def logoutview(request):
    logout(request)
    return render(request, 'votacao/index.html')
    # direccionar para página de sucesso


def register(request):
    return render(request, 'user/register.html')
