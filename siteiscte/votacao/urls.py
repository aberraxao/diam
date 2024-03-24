from django.urls import path
from . import views

app_name = 'votacao'
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('register', views.register, name='register'),
    path('informacao', views.informacao, name='informacao'),
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    path('<int:questao_id>/voto', views.votar_apagar_opcao, name='votar_apagar_opcao'),
    path('criarquestao', views.criarquestao, name='criarquestao'),
    path('<int:questao_id>/criaropcao', views.criaropcao, name='criaropcao'),
    path('<int:questao_id>/apagarquestao', views.apagarquestao, name='apagarquestao'),
]
