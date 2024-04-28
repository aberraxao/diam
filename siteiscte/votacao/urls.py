from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import LoginView

app_name = 'votacao'
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', views.logoutview, name='logout'),
    path('register', views.register, name='register'),
    path('informacao', TemplateView.as_view(template_name='votacao/profile.html'), name='informacao'),
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    path('<int:questao_id>/voto', views.voto, name='voto'),
    path('<int:questao_id>/apagar_opcao', views.apagar_opcao, name='apagar_opcao'),
    path('<int:questao_id>/criar_opcao', views.criar_opcao, name='criar_opcao'),
    path('<int:questao_id>/apagar_questao', views.apagar_questao, name='apagar_questao'),
    path('criar_questao', views.criar_questao, name='criar_questao'),
    path('fazer_upload', views.fazer_upload, name='fazer_upload'),
    path('api/questoes/', views.questoes),
]
