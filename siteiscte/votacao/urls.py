from django.urls import path
from . import views

# o '.' significa que importa views da mesma directoria)
urlpatterns = [
    path('', views.index, name='index'),

    # ex: votacao/3
    path('<int:questao_id>', views.detalhe, name='detalhe'),
]
