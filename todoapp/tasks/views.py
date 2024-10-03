from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404
from django.db.models import Avg,Count
from tasks.models import *
from tasks.forms import TaskForm # Make sure you create this form
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='users:landing-page')

def TaskList(request):
    tasks = Tasks.objects.filter(user=request.user).order_by("-created_at")
    
    context = {
        "tasks": tasks
    }
    
    return render(request, 'tasks/task_list.html', context)


def TaskCreate(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})

def TaskUpdate(request, pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)# pre fill the form with the current data
        if form.is_valid():
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm(instance=task) # if not post render the current for with the task details
    
    return render(request, 'tasks/edit_task.html', {'form': form})

def TaskDelete(request, pk):
    task =get_object_or_404(Tasks, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:index')
    return render(request, 'tasks/task_cofirm_delete.html', {'task': task})
    
    

def TaskDetail(request, pk):
    task = get_object_or_404(Tasks,pk=pk)
    return render(request, 'tasks/task_details.html', {'task': task})

def TaskToggle(request, pk):
    task = get_object_or_404(Tasks,pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('tasks:index')