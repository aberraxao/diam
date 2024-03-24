from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from votacao.models import Aluno

users = ["Maria", "Ana", "Rui", "Rita", "Joao", "Ines"]


def create_sample_users():
    for name in users:
        mail = name.lower() + "@iscte.pt"
        password = "pass"
        curso = "LEI-PL"

        if Aluno.objects.filter(username=name).exists():
            Aluno.objects.filter(username=name).update(email=mail, password=make_password(password), curso=curso)
        elif User.objects.filter(username=name).exists():
            User.objects.filter(username=name).update(email=mail, password=make_password(password))
        else:
            Aluno.objects.create_user(name, mail, password)


create_sample_users()
