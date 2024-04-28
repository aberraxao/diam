from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Questao, Opcao, Aluno, Imagem
from .serializers import QuestaoSerializer


def check_superuser(user):
    return user.is_superuser


@login_required
def index(request):
    context = {
        'latest_question_list': Questao.objects.order_by('-pub_data')[:10],
        'username': request.user.username
    }

    return render(request, 'votacao/index.html', context)


@require_http_methods(['GET'])
def logoutview(request):
    logout(request)
    return redirect('http://localhost:3000/votacao/login')


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
        comentario = request.POST.get('comentario', '')
        if not (username or email or password):
            return render(request, 'votacao/login.html', {'error_message': 'Preencher campos obrigatórios'})

        if comentario_invalido(comentario):
            return render(request, 'votacao/register.html', {'error_comentario': 'Já não se pode confiar'})

        if User.objects.filter(username=username).exists():
            return render(request, 'votacao/register.html', {'error_message': 'Utilizador já existe'})

        user = User.objects.create_user(
            username=username, email=email, password=password, first_name=nome, last_name=apelido
        )
        Aluno.objects.create(user=user, curso='LEI-PL-3', comentario=comentario)

        # return loginview(request)

    return render(request, 'votacao/register.html')


def comentario_invalido(comentario: str) -> bool:
    palavras_insultuosas = [
        'abécula', 'abentesma', 'achavascado', 'alimária', 'andrajoso',
        'barregã', 'biltre', 'cacóstomo', 'cuarra', 'estólido',
        'estroso', 'estultilóquio', 'nefelibata', 'néscio', 'pechenga',
        'sevandija', 'somítico', 'tatibitate', 'xexé', 'cheché',
        'xexelento'
    ]

    return any(palavra in comentario for palavra in palavras_insultuosas)


@login_required
def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)

    return render(request, 'votacao/detalhe.html', {'questao': questao})


@require_http_methods(['GET', 'POST'])
@user_passes_test(check_superuser)
def criar_questao(request):
    if request.method == 'POST':
        questao_texto = request.POST.get('novaquestao')
        if questao_texto:
            Questao(questao_texto=questao_texto, pub_data=timezone.now()).save()
    return render(request, 'votacao/criarquestao.html')


@require_http_methods(['GET', 'POST'])
@user_passes_test(check_superuser)
def criar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcao_texto = request.POST.get('novaopcao')
    if opcao_texto:
        questao.opcao_set.create(opcao_texto=opcao_texto).save()
    return render(request, 'votacao/criaropcao.html', {'questao': questao})


@require_http_methods(['POST'])
@user_passes_test(check_superuser)
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
        return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))


@require_http_methods(['POST'])
@user_passes_test(check_superuser)
def apagar_questao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    return HttpResponseRedirect(reverse('votacao:index'))


@require_http_methods(['POST'])
@login_required
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

        if request.user.opcao_set.count() >= 8 and not request.user.is_superuser:
            return render(request, 'votacao/detalhe.html', {
                'questao': questao,
                'error_message': 'Limite de votos atingido',
            })

        opcao.user.add(request.user)
        return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))


@require_http_methods(['GET'])
@login_required
def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcoes = get_object_or_404(Questao, pk=questao_id).opcao_set.annotate(count=Count('user'))
    return render(request, 'votacao/resultados.html', {'questao': questao, 'opcoes': opcoes})


@login_required
def fazer_upload(request):
    if request.method == 'POST' and request.FILES.get('myfile') is not None:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()

        if Imagem.objects.filter(user=request.user).exists():
            fs.delete(Imagem.objects.get(user=request.user).url)
        filename = fs.save(myfile.name, myfile)
        Imagem.objects.update_or_create(user=request.user, defaults={"url": filename})

        return render(request, 'votacao/profile.html')
    return render(request, 'votacao/fazer_upload.html')


@api_view(['GET', 'POST'])
def questoes(request):
    if request.method == 'GET':
        lista_questoes = Questao.objects.all()
        serializer = QuestaoSerializer(lista_questoes, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = QuestaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print(token)
            login(request, user)
            return JsonResponse({'token': token.key})
        else:
            return JsonResponse({'error': 'Credenciais inválidas'}, status=400)

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('votacao:index'))

        return redirect('http://localhost:3000/votacao/login')
