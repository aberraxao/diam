from django.contrib.auth.models import User

users = ["Maria", "Ana", "Rui", "Rita", "Joao", "Ines"]


def create_sample_users():
    for name in users:
        mail = name.lower() + "@iscte.pt"
        password = "pass"

        if User.objects.filter(username=name).exists():
            User.objects.filter(username=name).update(email=mail, password=password)
        else:
            User.objects.create_user(name, mail, password)


create_sample_users()
