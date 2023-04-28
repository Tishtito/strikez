from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('games/', views.games,name='game'),
    path('home2/' , views.home2, name='home2'),
    path('players/' , views.players, name='players'),
    path('players', views.show,name='players'),
    path('hall/', views.hall,name='hall'),
]
