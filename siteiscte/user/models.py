from django.contrib.auth.models import User
from django.db import models


class Aluno(User):
    curso = models.CharField(max_length=50)
