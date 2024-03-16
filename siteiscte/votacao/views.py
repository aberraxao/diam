from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods

from .models import Questao, Opcao
from django.urls import reverse


def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


@require_http_methods(["POST"])
def criarquestao(request):
    questao_texto = request.POST.get('novaquestao')
    if questao_texto:
        Questao(questao_texto=questao_texto, pub_data=timezone.now()).save()
    return render(request, 'votacao/criar_questao.html')


@require_http_methods(["POST"])
def criaropcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    opcao_texto = request.POST.get('novaopcao')
    if opcao_texto:
        questao.opcao_set.create(opcao_texto=opcao_texto, votos=0).save()
    return render(request, 'votacao/criar_opcao.html', {'questao': questao})


@require_http_methods(["POST"])
def apagaropcao(request, questao_id):
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


def apagarquestao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    return render(request, 'votacao/apagar_questao.html', {'questao': questao})


def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


@require_http_methods(["POST"])
def voto(request, questao_id):
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


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/resultados.html', {'questao': questao})
