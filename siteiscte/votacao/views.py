from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .models import Questao, Opcao, Aluno
from django.urls import reverse


@require_http_methods(['POST'])
def count_votes(request) -> int:
    return request.user.opcao_set.count()


@require_http_methods(['GET'])
def index(request):
    if not request.user.is_authenticated:
        return render(request, template_name='user/login.html')
    context = {}
    if request.GET.get('_method', '') == 'create_questao':
        if request.user.is_superuser:
            return render(request, 'votacao/criarquestao.html')
        else:
            context['error_message'] = 'Não tem permissões para efetuar esta operação'

    latest_question_list = Questao.objects.order_by('-pub_data')[:10]
    context['latest_question_list'] = latest_question_list
    context['username'] = request.user.username

    return render(request, 'votacao/index.html', context)


@require_http_methods(['GET', 'POST'])
def loginview(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('votacao:index'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            return render(request, 'user/login.html', {'error_message': 'Utilizador não encontrado'})

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'user/login.html', {'error_message': 'Password errada'})

        login(request, user)
        request.session['USERNAME'] = user.username
        request.session['EMAIL'] = user.email
        request.session['FULL_NAME'] = user.get_full_name()
        aluno = Aluno.objects.filter(user__username=request.user.username).first()
        request.session['CURSO'] = aluno.curso if aluno else 'Não inscrito'
        request.session['VOTOS'] = count_votes(request)

        return HttpResponseRedirect(reverse('votacao:index'))

    return render(request, 'user/login.html')


@require_http_methods(['GET'])
def logoutview(request):
    logout(request)
    return render(request, template_name='user/login.html')


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
        grupo = request.POST.get('grupo', '')
        if not (username or email or password):
            return render(request, 'user/login.html', {'error_message': 'Preencher campos obrigatórios'})
        if User.objects.filter(username=username).exists():
            return render(request, 'user/register.html', {'error_message': 'Utilizador já existe'})

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=nome, last_name=apelido
        )

        if grupo:
            curso_grupo, _ = Group.objects.get_or_create(name=f"{curso}-{grupo}")
            user.group = curso_grupo

        Aluno.objects.create(user=user, curso=curso)

        return loginview(request)

    return render(request, 'user/register.html')


@require_http_methods(['GET', 'POST'])
def criarquestao(request):
    if not request.user.is_authenticated:
        return render(request, template_name='user/login.html')

    if request.method == 'POST':
        questao_texto = request.POST.get('novaquestao')
        if questao_texto:
            Questao(questao_texto=questao_texto, pub_data=timezone.now()).save()
    return render(request, 'votacao/criarquestao.html')


@require_http_methods(['GET', 'POST'])
def detalhe(request, questao_id):
    if not request.user.is_authenticated:
        return render(request, template_name='user/login.html')

    questao = get_object_or_404(Questao, pk=questao_id)

    if 'delete' in request.POST.get('_method', '') or 'create' in request.GET.get('_method', ''):
        if not request.user.is_superuser:
            return render(request, 'votacao/detalhe.html',
                          {'questao': questao, 'error_message': 'Não tem permissões para efetuar a operação'})

        if request.POST.get('_method', '') == 'delete_questao':
            questao.delete()
            request.session['VOTOS'] = count_votes(request)
            return HttpResponseRedirect(reverse('votacao:index'))

        elif request.POST.get('_method', '') == 'delete_opcao':
            try:
                opcao = questao.opcao_set.get(pk=request.POST['opcao'])
            except (KeyError, Opcao.DoesNotExist):
                return render(request, 'votacao/detalhe.html', {
                    'questao': questao,
                    'error_message': 'Não escolheu uma opção',
                })
            else:
                opcao.delete()
                request.session['VOTOS'] = count_votes(request)
                return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))

        elif request.GET.get('_method', '') == 'create_opcao':
            opcao_texto = request.POST.get('novaopcao')
            if opcao_texto:
                questao.opcao_set.create(opcao_texto=opcao_texto).save()
            return render(request, 'votacao/criaropcao.html', {'questao': questao})

    return render(request, 'votacao/detalhe.html', {'questao': questao})


@require_http_methods(['POST'])
def votar(request, questao_id):
    if not request.user.is_authenticated:
        return render(request, template_name='user/login.html')

    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(request, 'votacao/detalhe.html', {
            'questao': questao,
            'error_message': 'Não escolheu uma opção',
        })
    else:
        if opcao.user.filter(username=request.user).exists():
            return render(request, 'votacao/detalhe.html', {
                'questao': questao,
                'error_message': 'Só pode votar uma vez em cada opção',
            })
        opcao.user.add(request.user)
        request.session['VOTOS'] = count_votes(request)
        return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))


@require_http_methods(['GET'])
def resultados(request, questao_id):
    if not request.user.is_authenticated:
        return render(request, template_name='user/login.html')

    questao = get_object_or_404(Questao, pk=questao_id)
    opcoes = get_object_or_404(Questao, pk=questao_id).opcao_set.annotate(count=Count('user'))
    return render(request, 'votacao/resultados.html', {'questao': questao, 'opcoes': opcoes})
