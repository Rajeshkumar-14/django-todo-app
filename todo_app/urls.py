from django.urls import path
from . import views

__project_by__ = "RajeshKumar"

urlpatterns = [
    path("", views.index, name="index"),
    path("get-tasks/", views.TaskView.as_view(), name="get-tasks"),
    path("create-task/", views.create_task, name="create-task"),
    path("edit-task/<int:id>", views.edit_task, name="edit-task"),
    path("update-task/<int:id>", views.update_task, name="update-task"),
    path("delete-task/<int:id>", views.delete_task, name="delete-task"),
    path("display-task/<int:id>", views.display_task, name="display-task"),
    path("task-complete/<int:id>", views.task_complete, name="task-complete"),
]
