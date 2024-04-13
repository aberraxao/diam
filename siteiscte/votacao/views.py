from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.urls import reverse, reverse_lazy

from .models import Questao, Opcao, Aluno


def check_superuser(user):
    return user.is_superuser


@require_http_methods(['POST'])
def count_votes(request) -> int:
    return request.user.opcao_set.count()


@login_required(login_url=reverse_lazy('votacao:login'))
def index(request):
    context = {
        'latest_question_list': Questao.objects.order_by('-pub_data')[:10],
        'username': request.user.username
    }

    return render(request, 'votacao/index.html', context)


@require_http_methods(['GET', 'POST'])
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            return render(request, 'votacao/login.html', {'error_message': 'Utilizador não encontrado'})

        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, 'votacao/login.html', {'error_message': 'Password errada'})

        login(request, user)
        request.session['USERNAME'] = user.username
        request.session['EMAIL'] = user.email
        request.session['FULL_NAME'] = user.get_full_name() if not None else user.username
        aluno = Aluno.objects.filter(user__username=request.user.username).first()
        request.session['CURSO'] = aluno.curso if aluno else 'Não inscrito'
        request.session['VOTOS'] = count_votes(request)
        request.session['PICTURE'] = get_profile_picture(user.username)

        return HttpResponseRedirect(reverse('votacao:index'))

    return render(request, 'votacao/login.html')


def get_profile_picture(username: str):
    fs = FileSystemStorage()
    if fs.exists(username):
        return fs.url(username)

    return 'static/media/profile.png'


@require_http_methods(['GET'])
def logoutview(request):
    logout(request)
    return render(request, template_name='votacao/login.html')


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
        if not (username or email or password):
            return render(request, 'votacao/login.html', {'error_message': 'Preencher campos obrigatórios'})
        if User.objects.filter(username=username).exists():
            return render(request, 'votacao/register.html', {'error_message': 'Utilizador já existe'})

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=nome, last_name=apelido
        )

        Aluno.objects.create(user=user, curso="LEI-PL-3")

        return loginview(request)

    return render(request, 'votacao/register.html')


@login_required(login_url=reverse_lazy('votacao:login'))
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)

    return render(request, 'votacao/detalhe.html', {'questao': questao})


@require_http_methods(['GET'])
@user_passes_test(check_superuser, redirect_field_name="votacao:login")
def criar_questao(request):
    return render(request, 'votacao/criarquestao.html')


@require_http_methods(['POST'])
@user_passes_test(check_superuser, redirect_field_name="votacao:login")
def gravar_questao(request):
    questao_texto = request.POST.get('novaquestao')
    if questao_texto:
        Questao(questao_texto=questao_texto, pub_data=timezone.now()).save()
    return render(request, 'votacao/criarquestao.html')


@require_http_methods(['GET', 'POST'])
@user_passes_test(check_superuser, redirect_field_name="votacao:login")
def criar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcao_texto = request.POST.get('novaopcao')
    if opcao_texto:
        questao.opcao_set.create(opcao_texto=opcao_texto).save()
    return render(request, 'votacao/criaropcao.html', {'questao': questao})


@require_http_methods(['POST'])
@user_passes_test(check_superuser, redirect_field_name="votacao:login")
def apagar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
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


@require_http_methods(['POST'])
@user_passes_test(check_superuser, redirect_field_name="votacao:login")
def apagar_questao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    request.session['VOTOS'] = count_votes(request)
    return HttpResponseRedirect(reverse('votacao:index'))


@require_http_methods(['POST'])
@login_required(login_url=reverse_lazy('votacao:login'))
def voto(request, questao_id):
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

        if count_votes(request) >= 8 and not request.user.is_superuser:
            return render(request, 'votacao/detalhe.html', {
                'questao': questao,
                'error_message': 'Limite de votos atingido',
            })

        opcao.user.add(request.user)
        request.session['VOTOS'] = count_votes(request)
        return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))


@require_http_methods(['GET'])
@login_required(login_url=reverse_lazy('votacao:login'))
def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcoes = get_object_or_404(Questao, pk=questao_id).opcao_set.annotate(count=Count('user'))
    return render(request, 'votacao/resultados.html', {'questao': questao, 'opcoes': opcoes})


@login_required(login_url=reverse_lazy('votacao:login'))
def fazer_upload(request):
    if request.method == 'POST' and request.FILES.get('myfile') is not None:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.delete(request.user.username)
        fs.save(request.user.username, myfile)
        request.session['PICTURE'] = fs.url(request.user.username)
        return render(request, 'votacao/profile.html', )
    return render(request, 'votacao/fazer_upload.html')
