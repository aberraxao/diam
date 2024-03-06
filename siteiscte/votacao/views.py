from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,world. Esta é a página de entrada da app votação.")
