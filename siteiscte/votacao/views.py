from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Esta é a página de entrada da app votacao</h1>")
