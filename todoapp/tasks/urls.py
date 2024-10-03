from django.urls import path

app_name = "tasks"

from .views import *

urlpatterns = [
    path('', TaskList, name="index"),
    path("<int:pk>/", TaskDetail, name="task-detail"),
    path("create/", TaskCreate, name="task-create"),
    path("update/<int:pk>/", TaskUpdate, name="task-update"),
    path("delete/<int:pk>/", TaskDelete, name="task-delete"),
    path("toggle/<int:pk>/",TaskToggle, name='task-toggle'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>', TaskDetailAPIView.as_view(), name='task-detail')
]