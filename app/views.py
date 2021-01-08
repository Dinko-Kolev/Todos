from django.shortcuts import render, redirect

from app.forms import TaskForm, TaskDeleteForm
from app.models import Task


def index(request):
    if request.method == 'GET':
        context = {
            'form': TaskForm,
            'tasks': Task.objects.all(),
        }
        return render(request, 'index.html', context)
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'tasks': Task.objects.all(),
        'form': form,
    }
    return render(request, 'index.html', context)


def edit(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'tasks': Task.objects.all(),
        'form': form,
    }
    return render(request, 'edit_task.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskDeleteForm(instance=task)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        context = {
            'tasks': Task.objects.all(),
            'form': form,
            'task':task,
        }
        return render(request, 'delete_task.html', context)
