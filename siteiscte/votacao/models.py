from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.utils import timezone
import datetime

from siteiscte.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    curso = models.CharField(max_length=100)
    comentario = models.TextField(null=True)

    def __str__(self):
        return self.user.get_full_name() if not None else self.user.get_username()


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


class Imagem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True)


class PalavraProibida(models.Model):
    palavra = models.CharField(max_length=200)
