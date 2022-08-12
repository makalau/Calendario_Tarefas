from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tarefas', views.tarefas),
    path('relatorios', views.relatorios),
]
