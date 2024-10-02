from django.urls import path

app_name = "tasks"

from . import views

urlpatterns = [
    path('', views.TaskList, name="index"),
    path("<int:pk>/", views.TaskDetail, name="task-detail"),
    path("create/", views.TaskCreate, name="task-create"),
    path("update/<int:pk>/", views.TaskUpdate, name="task-update"),
    path("delete/<int:pk>/", views.TaskDelete, name="task-delete"),
]