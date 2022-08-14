from django.shortcuts import render
from .forms import TaskForm

def home(request):
    return render(request, 'index.html')


def tarefa(request):
    form = TaskForm()
    return render(request, "tarefa.html", {"form": form})


def relatorios(request):
    return render(request, "relatorio.html")

def editar(request):
    return render(request, "editar.html")
