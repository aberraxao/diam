from datetime import timedelta

from votacao.models import Questao
from django.utils import timezone

from django.contrib.auth.models import User, Group

from votacao.models import Aluno

users = ["Maria", "Ana", "Rui", "Rita", "Joao", "Ines"]
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


def show_questions() -> None:
    for line in Questao.objects.all():
        print(line)


def show_options_started_with(text: str) -> None:
    for line in Questao.objects.get(questao_texto__startswith=text).opcao_set.all():
        print(line)


def recent_questions(years: int) -> None:
    now = timezone.now()
    then = now - timedelta(days=365 * years)
    for line in Questao.objects.filter(pub_data__gte=then):
        print(line)


def create_questions() -> None:
    for questao, opcoes in questoes.items():
        q = Questao(questao_texto=questao, pub_data=timezone.now())
        q.save()
        for opcao in opcoes:
            q.opcao_set.create(opcao_texto=opcao[0])


def create_users() -> None:
    for name in users:
        if not User.objects.filter(username=name).exists():
            user = User.objects.create_user(name, email=f"{name.lower()}@iscte.pt", password="pass")
            curso, _ = Group.objects.get_or_create(name="LEI-PL-3")
            user.groups.add(curso)
            Aluno.objects.create(user=user, curso=curso)


def create_superuser() -> None:
    User.objects.create_superuser(username='admin', email='admin', password='admin')


def create_db() -> None:
    create_superuser()
    create_users()
    create_questions()


def delete_all() -> None:
    Questao.objects.all().delete()
    User.objects.all().delete()
    Group.objects.all().delete()


delete_all()
create_db()

print("\nalínea a) Mostrar uma lista com o texto de todas as questões em BD.\n")
show_questions()

print("\nalínea b) Mostrar as opções da questão em que o texto começa com 'Gostas de...'.\n")
show_options_started_with("Gostas de")

print("\nalínea d) Mostrar uma lista das questões publicadas nos últimos 3 anos.\n")
then = timezone.now() - timedelta(days=365 * 10)  # 10 years ago
q = Questao.objects.get(questao_texto__startswith="Quest")
q.pub_data = then
q.save()
recent_questions(3)
