from django.urls import path
from django.views.generic import RedirectView

from user import views

app_name = 'user'
urlpatterns = [
    path('', RedirectView.as_view(url='/user/login'), name='index'),
    path('login', views.loginview, name='login'),
    path('logout', views.logoutview, name='logout'),
    path('register', views.registerview, name='register'),
]
