from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import Questao, Opcao


def index(request):
    latest_question_list = Questao.objects.order_by('-pub_data')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'votacao/index.html', context)


def detalhe(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request, 'votacao/detalhe.html', {'questao': questao})


def resultados(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    return render(request,'votacao/resultados.html', {'questao': questao})


def voto(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para votar
        return render(request, 'votacao/detalhe.html', {'questao': questao,'error_message': "Não escolheu uma opção",})
    else:
        opcao_seleccionada.votos += 1
        opcao_seleccionada.save()
        # Retorne sempre HttpResponseRedirect depois de
        # tratar os dados POST de um form
        # pois isso impede os dados de serem tratados
        # repetidamente se o utilizador
        # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:resultados', args=(questao.id,)))


def criar_questao(request):
    try:
        novaQuestao =''
        novaQuestao = Questao(questao_texto=(request.POST['questaoNova']), pub_data=timezone.now())
    except (KeyError, Questao.DoesNotExist):
        # Apresenta de novo o form para inserir questao
        return render(request, 'votacao/criar_questao.html',
                      {'questao': novaQuestao, 'error_message': "Não inseriu nenhuma pergunta", })
    else:
        novaQuestao.save()
        # Retorne sempre HttpResponseRedirect depois de
        # tratar os dados POST de um form
        # pois isso impede os dados de serem tratados
        # repetidamente se o utilizador
        # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:index', args=()))


def criar_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:

        novaOpcao = questao.opcao_set.create(opcao_texto=(request.POST['novaOpcao']),votos=0)
    except (KeyError, Opcao.DoesNotExist):
        # Apresenta de novo o form para inserir opcao
        return render(request, 'votacao/criar_opcao.html', {'questao': questao, 'error_message': "Não inseriu nenhuma opção", })
    else:
        novaOpcao.save()
        # Retorne sempre HttpResponseRedirect depois de
        # tratar os dados POST de um form
        # pois isso impede os dados de serem tratados
        # repetidamente se o utilizador
        # voltar para a página web anterior.
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))


def remover_questao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    questao.delete()
    return HttpResponseRedirect(reverse('votacao:index', args=()))


def remover_opcao(request, questao_id):
    questao = get_object_or_404(Questao, pk=questao_id)
    try:
        opcao_seleccionada = questao.opcao_set.get(pk=request.POST['opcao'])
    except (KeyError, Opcao.DoesNotExist):
        return render(
            request,
            'votacao/detalhe.html',
            {'questao': questao, 'error_message': "Não escolheu uma opção", }
        )
    else:
        opcao_seleccionada.delete()
    return HttpResponseRedirect(reverse('votacao:detalhe', args=(questao.id,)))
