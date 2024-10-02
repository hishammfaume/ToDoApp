from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404
from django.db.models import Avg,Count
from tasks.models import *
from tasks.forms import TaskForm # Make sure you create this form
# Create your views here.


def TaskList(request):
    tasks = Tasks.objects.all().order_by("-created_at")
    
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
            return redirect('list_tasks')
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})

def TaskUpdate(request, pk):
    task = get_object_or_404(Tasks,pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if
    pass

def TaskDelete(request):
    pass

def TaskDetail(request):
    pass