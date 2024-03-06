from django.urls import path
from . import views

# o '.' significa que importa views da mesma directoria)
urlpatterns = [
    path('', views.index, name='index'),
]
