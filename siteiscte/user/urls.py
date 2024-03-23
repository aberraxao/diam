from django.urls import path
from django.views.generic import RedirectView

from user import views

app_name = 'user'
urlpatterns = [
    path('', RedirectView.as_view(url='/user/home')),
    path('home', views.home, name='home'),
    path('login', views.loginview, name='login'),
    path('register', views.register, name='register'),
]
