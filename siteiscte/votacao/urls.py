from django.urls import path
from . import views

app_name = 'votacao'
urlpatterns = [
    # ex: votacao/
    path('', views.index, name='index'),
    # ex: votacao/1
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    # ex: votacao/3/resultados
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    # ex: votacao/3/voto
    path('<int:questao_id>/voto', views.voto, name='voto'),
    # ex: votacao/criarquestao
    path('criarquestao', views.criar_questao, name='criarquestao'),
    # ex: votacao/3/criaropcao
    path('<int:questao_id>/criaropcao', views.criar_opcao, name='criaropcao'),
    path('<int:questao_id>/removerquestao', views.remover_questao, name='removerquestao'),
    path('<int:questao_id>/removeropcao', views.remover_opcao, name='removeropcao'),
]
