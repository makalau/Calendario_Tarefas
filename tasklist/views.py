from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Tarefas

def home(request):
    search = request.GET.get("search")
    if search:
        consulta = Tarefas.objects.all().filter(title__icontains=search)
        return render(request, 'index.html', {"consulta": consulta})
    else:
        return render(request, 'index.html')



def taskview(request, id):
    task = get_object_or_404(Tarefas, pk=id)
    return render(request, 'task.html', {"task": task})

def tarefa(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        new_task = Tarefas(title=title, description=description)
        new_task.save()
        return redirect("/")

    else:
        return render(request, "tarefa.html")


def relatorios(request):
    return render(request, "relatorio.html")


def editar(request, id):
    consulta = get_object_or_404(Tarefas, pk=id)
    form = TaskForm(instance=consulta)   
    if request.method == "POST":
        form = TaskForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta.save()
            return redirect("/")
        else:
            return render(request, "editar.html", {"form":form, "consulta":consulta})
    else:
        return render(request, "editar.html", {"form":form, "consulta":consulta})


def deletar(request, id):
    campo = get_object_or_404(Tarefas, pk=id)
    campo.delete()
    return redirect('/')
