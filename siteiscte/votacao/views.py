from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .models import Questao, Opcao, Aluno
from django.urls import reverse


@require_http_methods(["POST"])
def count_votes(request) -> int:
    return Votos.objects.filter.aggregate(sum_votos=Sum("votos", default=0)).get("sum_votos")


def index(request):
    if request.user.is_authenticated:
        latest_question_list = Questao.objects.order_by('-pub_data')[:10]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'votacao/index.html', context)
    return render(request, template_name='user/login.html')


@require_http_methods(['GET', 'POST'])
def loginview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('votacao:index'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
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
def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('votacao:index'))

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        nome = request.POST.get('nome', '')
        apelido = request.POST.get('apelido', '')
        email = request.POST.get('email', '')
        curso = request.POST.get('curso', '')
        if not (username or email or password):
            return render(request, 'user/login.html', {'error_message': "Preencher campos obrigatórios"})
        if User.objects.filter(username=username).exists():
            return render(request, 'user/register.html', {'error_message': "Utilizador já existe"})

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=nome, last_name=apelido
        )
        Aluno.objects.create(user=user, curso=curso)
        return loginview(request)

    return render(request, 'user/register.html')


def informacao(request):
    if request.user.is_authenticated:
        user = Aluno.objects.filter(user__username=request.user.username).first()
        curso = user.curso if user else ''

        return render(request, 'user/informacao.html', {'curso': curso})

    return render(request, 'user/login.html')


@require_http_methods(["POST"])
def criarquestao(request):
    if request.user.is_authenticated:
        questao_texto = request.POST.get('novaquestao')
        if questao_texto:
            Questao(questao_texto=questao_texto, pub_data=timezone.now()).save()
        return render(request, 'votacao/criarquestao.html')
    return render(request, 'user/login.html')


@require_http_methods(["POST"])
def criaropcao(request, questao_id):
    if request.user.is_authenticated:
        questao = get_object_or_404(Questao, pk=questao_id)
        opcao_texto = request.POST.get('novaopcao')
        if opcao_texto:
            questao.opcao_set.create(opcao_texto=opcao_texto, votos=0).save()
        return render(request, 'votacao/criaropcao.html', {'questao': questao})
    return render(request, 'user/login.html')


@require_http_methods(["POST"])
def apagaropcao(request, questao_id):
    if request.user.is_authenticated:
        questao = get_object_or_404(Questao, pk=questao_id)
        try:
            opcao_selecionada = questao.opcao_set.get(pk=request.POST['opcao'])
        except (KeyError, Opcao.DoesNotExist):
            return render(
                request,
                'votacao/detalhe.html',
                {'questao': questao, 'error_message': "Não escolheu uma opção", }
            )
        else:
            opcao_selecionada.delete()
        return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))
    return render(request, 'user/login.html')


def apagarquestao(request, questao_id):
    if request.user.is_authenticated:
        questao = get_object_or_404(Questao, pk=questao_id)
        questao.delete()
    return HttpResponseRedirect(reverse('votacao:index'))


def detalhe(request, questao_id):
    if request.user.is_authenticated:
        questao = get_object_or_404(Questao, pk=questao_id)
        return render(request, 'votacao/detalhe.html', {'questao': questao})
    return render(request, 'user/login.html')


@require_http_methods(["POST"])
def voto(request, questao_id):
    if request.user.is_authenticated:
        questao = get_object_or_404(Questao, pk=questao_id)
        try:
            opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
        except (KeyError, Opcao.DoesNotExist):
            return render(request, 'votacao/detalhe.html', {
                'questao': questao,
                'error_message': "Não escolheu uma opção",
            })
        else:
            opcao_seleccionada.votos += 1
            opcao_seleccionada.save()
        return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))
    return render(request, 'user/login.html')


def resultados(request, questao_id):
    if request.user.is_authenticated:
        questao = get_object_or_404(Questao, pk=questao_id)
        return render(request, 'votacao/resultados.html', {'questao': questao})
    return render(request, 'user/login.html')
