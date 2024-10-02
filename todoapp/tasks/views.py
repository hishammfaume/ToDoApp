from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404
from django.db.models import Avg,Count
from .models import *
from .forms import TaskForm # Make sure you create this form
# Create your views here.


def list_tasks(request):
    tasks = Tasks.objects.all().order_by("-created_at")
    
    context = {
        "tasks": tasks
    }
    
    return render(request, 'task_list.html', context)


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('list_tasks')
    else:
        form = TaskForm()
    
    return render(request, 'task_form,html', {'form': form})

