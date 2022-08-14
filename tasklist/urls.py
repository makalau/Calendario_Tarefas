from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tarefa', views.tarefa),
    path('relatorios', views.relatorios),
    path('editar', views.editar),
]
