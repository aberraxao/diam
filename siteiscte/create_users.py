from django.contrib.auth.models import User

from user.models import Aluno

users = ["Maria", "Ana", "Rui", "Rita", "Joao", "Ines"]


def create_sample_users():
    for name in users:
        mail = name.lower() + "@iscte.pt"
        password = "pass"

        if Aluno.objects.filter(username=name).exists():
            Aluno.objects.filter(username=name).update(email=mail, password=password)
        else:
            Aluno.objects.create_user(name, mail, password)


create_sample_users()
