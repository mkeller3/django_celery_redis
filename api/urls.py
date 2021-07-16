from django.urls import path
from . import views

urlpatterns = [
    path('generate_task/', views.GenerateTask.as_view(), name="generate_task"),
    path('task_status/', views.TaskStatus.as_view(), name="task_status"),
    path('task_result/', views.TaskResult.as_view(), name="task_result"),
]