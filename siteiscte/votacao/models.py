from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()


class Questao(models.Model):
    questao_texto = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data de publicacao')

    def __str__(self):
        return self.questao_texto

    def foi_publicada_recentemente(self):
        return self.pub_data >= timezone.now() - datetime.timedelta(days=1)


class Opcao(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    opcao_texto = models.CharField(max_length=200)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.opcao_texto


class PalavraProibida(models.Model):
    palavra = models.CharField(max_length=200)
