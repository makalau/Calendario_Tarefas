from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def tarefas(request):
    return render(request, "tarefas.html")


def relatorios(request):
    return render(request, "relatorios.html")