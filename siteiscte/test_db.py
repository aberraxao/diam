from django.utils import timezone

from votacao.models import Questao

questoes = {
    'Gostas de DIAM?': ['Sim', 'Não'],
    'Gostas de programar?': ['Sim', 'Não'],
    'És de que clube?': ['Sim', 'Não']
}


def create_samples():
    for q_texto, opcoes in questoes.items():
        questao = Questao(questao_texto=q_texto, pub_data=timezone.now())
        questao.save()
        for o_texto in opcoes:
            questao.opcao_set.create(opcao_texto=o_texto)


def delete_all():
    questoes = Questao.objects.all()
    for questao in questoes:
        questao.delete()


delete_all()
create_samples()
