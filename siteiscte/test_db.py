from datetime import timedelta
from votacao.models import Questao, Opcao
from django.utils import timezone
from django.db.models import Sum


def delete_all():
    questoes = Questao.objects.all()
    for questao in questoes:
        questao.delete()


def show_questions():
    for line in Questao.objects.all():
        print(line)


def show_options_started_with(text: str) -> None:
    for line in Questao.objects.get(questao_texto__startswith=text).opcao_set.all():
        print(line)


def show_options(start: str, nb: int) -> None:
    q = Questao.objects.get(questao_texto__startswith=start)
    for line in q.opcao_set.filter(votos__gt=nb):
        print(line)


def recent_questions(years: int) -> None:
    now = timezone.now()
    then = now - timedelta(days=365 * years)
    for line in Questao.objects.filter(pub_data__gte=then):
        print(line)


def count_votes() -> int:
    return Opcao.objects.aggregate(sum_votos=Sum("votos", default=0)).get("sum_votos")


def more_votes() -> None:
    for questao in Questao.objects.all():
        print(questao)
        # get_most_voted(questao)
        print("Opção mais votada: ", get_most_voted(questao), "\n")


def get_most_voted(q: Questao) -> str:
    return q.opcao_set.order_by('-votos').first()


questoes = {"Vamos fazer uma festa no fim do ano?": [["Sim."],
                                                     ["Não."],
                                                     ["Talvez."],
                                                     ],
            "Gostas de gatos?": [["Miauuuu ..."],
                                 ["Adoro."],
                                 ["Que fofos"],
                                 ["Sim, claro!"],
                                 ],
            "Questão muito antiga: Quo vadis?": [["A todo o lado."],
                                                 ["Rumo ao infinito."],
                                                 ],
            }


def create_db() -> None:
    for questao, opcoes in questoes.items():
        q = Questao(questao_texto=questao, pub_data=timezone.now())
        q.save()
        for opcao in opcoes:
            q.opcao_set.create(opcao_texto=opcao[0], votos=opcao[1])


delete_all()
create_db()

# alínea a)
print("\nalínea a) Mostrar uma lista com o texto de todas as questões em BD.\n")
show_questions()

# alínea b)
print("\nalínea b) Mostrar as opções da questão em que o texto começa com 'Gostas de...'.\n")
show_options_started_with("Gostas de")

# alínea c)
print("\nalínea c) Mostrar as opções com número de votos superior a 2 da questão em que o texto \
começa com 'Gostas de...'.\n")
show_options("Gostas de", 2)

# alínea d)
print("\nalínea d) Mostrar uma lista das questões publicadas nos últimos 3 anos.\n")
then = timezone.now() - timedelta(days=365 * 10)  # 10 years ago
q = Questao.objects.get(questao_texto__startswith="Quest")
q.pub_data = then
q.save()
recent_questions(3)  # we changed the "pub_data" field before

# alínea e)
print("\nalínea e) Calcular e mostrar o número total de votos que estão registados na base de dados.\n")
print(count_votes())

# alínea f)
print("\nalínea f) Percorrer todas as questões da DB e, para cada uma, mostrar o texto da questão \
e o da opção que tiver mais votos.\n")
more_votes()
