from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from votacao.models import Aluno

users = ["Maria", "Ana", "Rui", "Rita", "Joao", "Ines"]


def create_sample_users():
    for name in users:
        mail = name.lower() + "@iscte.pt"
        password = "pass"
        curso = "LEI-PL"

        if User.objects.filter(username=name).exists():
            user = User.objects.filter(username=name)
            user.update(email=mail, password=make_password(password))
            Aluno.objects.update_or_create(user=user.first(), curso=curso)
        else:
            user = User.objects.create_user(name, mail, password)
            Aluno.objects.create(user=user, curso=curso)


create_sample_users()
