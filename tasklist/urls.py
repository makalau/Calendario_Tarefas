from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('task/<int:id>', views.taskview),
    path('tarefa', views.tarefa),
    path('relatorios', views.relatorios),
    path('editar', views.editar),
]
