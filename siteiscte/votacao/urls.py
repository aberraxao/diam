from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'votacao'
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('register', views.register, name='register'),
    path('informacao', TemplateView.as_view(template_name='user/informacao.html'), name='informacao'),
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    path('<int:questao_id>/voto', views.voto, name='voto'),
    path('criarquestao', views.criarquestao, name='criarquestao'),
]
