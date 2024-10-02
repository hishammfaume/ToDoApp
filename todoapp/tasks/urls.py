from django.urls import path

app_name = "tasks"

from . import views

urlpatterns = [
    path('', views.TaskList, name="index"),
    path("<int:pk>/", views.TaskDetail, name="task-detail"),
    path("create/", views.TaskCreate, name="task-create"),
    path("<int:pk>/update/", views.TaskUpdate, name="task-update"),
    path("<int:pk>/delete/", views.TaskDelete, name="task-delete"),
]