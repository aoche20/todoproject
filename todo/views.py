from django.shortcuts import render,redirect,get_object_or_404
from .models   import Task
from .forms import TaskForm
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request,'todo/index.html', context={'tasks':tasks})


def task_create(request):
    if request.method == "POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form=TaskForm()
    return render(request,'todo/task_form.html', context={'form':form})     


def task_update(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method =='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task) 
    return render(request,'todo/task_form.html', context={'form':form})      

def task_delete(request,id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('task_list')
