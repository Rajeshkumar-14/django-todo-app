from http.client import INTERNAL_SERVER_ERROR
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Todo

from ajax_datatable.views import AjaxDatatableView
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

__project_by__ = "RajeshKumar"


class TaskView(LoginRequiredMixin, AjaxDatatableView):
    model = Todo
    show_column_filters = False
    length_menu = [[5, 10, 15, 20], [5, 10, 15, 20]]

    column_defs = [
        {
            "name": "id",
            "visible": False,
            "searchable": False,
            "orderable": False,
            "className": "text-center",
        },
        {
            "name": "title",
            "visible": True,
            "searchable": True,
            "orderable": True,
            "className": "text-center",
        },
        {
            "name": "description",
            "visible": True,
            "searchable": False,
            "orderable": False,
            "className": "text-center",
        },
        {
            "name": "status",
            "visible": True,
            "searchable": True,
            "orderable": True,
            "className": "text-center",
        },
        {
            "name": "time_ago_created_at",
            "title": "Created At",
            "visible": True,
            "searchable": False,
            "orderable": True,
            "className": "text-center",
        },
        {
            "name": "action_1",
            "title": "View & Mark",
            "visible": True,
            "searchable": False,
            "orderable": False,
            "className": "text-center action-column",
        },
        {
            "name": "action_2",
            "title": "Edit & Delete",
            "visible": True,
            "searchable": False,
            "orderable": False,
            "className": "text-center action-column",
        },
    ]

    def customize_row(self, row, obj):
        action_buttons_2 = ""
        action_buttons_1 = ""

        # Check if the task status is "Completed" and disable the "Mark Complete" button accordingly
        if obj.status != "Completed":
            action_buttons_1 += f'<div class="btn-group">'
            action_buttons_1 += f'<button class="btn btn-custom task-view-btn me-1" data-task-id="{obj.id}"><i class="fa-solid fa-eye p-2"></i></button>'
            action_buttons_1 += f'<button class="btn btn-success mark-complete-btn" data-task-id="{obj.id}"><i class="fa-solid fa-circle-check p-2"></i></button>'
            action_buttons_1 += f"</div>"
        else:
            action_buttons_1 += f'<button class="btn w-100 btn-custom task-view-btn me-1" data-task-id="{obj.id}"><i class="fa-solid fa-eye p-2"></i></button>'
        row["action_1"] = action_buttons_1

        if obj.status != "Completed":
            action_buttons_2 += f'<div class="btn-group">'
            action_buttons_2 += f'<button class="btn btn-secondary task-edit-btn me-1" data-task-id="{obj.id}"><i class="fa-solid fa-pen-to-square p-2"></i></button>'
            action_buttons_2 += f'<button class="btn btn-danger task-delete-btn " data-task-id="{obj.id}"><i class="fa-solid fa-trash p-2"></i></button>'
            action_buttons_2 += f"</div>"
        else:
            action_buttons_2 += f'<button class="btn w-100 btn-danger task-delete-btn" data-task-id="{obj.id}"><i class="fa-solid fa-trash p-2"></i></button>'

        row["action_2"] = action_buttons_2

        return row


@login_required(login_url="login")
def index(request):
    return render(request, "todo/index.html")


@login_required(login_url="login")
def create_task(request):
    user = request.user

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        if Todo.objects.filter(title=title).exists():
            return JsonResponse(
                {"status": "error", "message": "A Task's Title already Exists"},
                status=400,
            )
        else:
            task = Todo.objects.create(user=user, title=title, description=description)
            return JsonResponse(
                {"status": "success", "message": "Task saved successfully"}, status=201
            )

    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=400
    )


@login_required(login_url="login")
def edit_task(request, id):
    try:
        task = get_object_or_404(Todo, id=id)
        data = {
            "id": task.id,
            "title": task.title,
            "description": task.description,
        }
        return JsonResponse(data, status=200)
    except Todo.DoesNotExist:
        return JsonResponse({"status": "error"}, status=404)


def update_task(request, id):
    task = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        title = request.POST.get("edit-title")
        description = request.POST.get("edit-description")
        task.title = title
        task.description = description
        task.updated_at = timezone.now()
        task.save()
        return JsonResponse(
            {"status": "success", "message": "Task updated successfully"}
        )

    return JsonResponse({"status": "error", "message": "Invalid request method"})


@login_required(login_url="login")
def delete_task(request, id):
    try:
        task = get_object_or_404(Todo, id=id)
        try:
            task.delete()
            return JsonResponse({"status": "success"}, status=200)
        except INTERNAL_SERVER_ERROR:
            return JsonResponse({"status": "error"}, status=500)
    except Todo.DoesNotExist:
        return JsonResponse({"status": "error"}, status=404)


@login_required(login_url="login")
def task_complete(request, id):
    try:
        task = get_object_or_404(Todo, id=id)
        try:
            task.status = "Completed"
            task.updated_at = timezone.now()
            task.save()
            return JsonResponse(
                {"status": "success", "message": "Task Completed"}, status=200
            )
        except INTERNAL_SERVER_ERROR:
            return JsonResponse(
                {"status": "error", "message": "Internal Server Error"}, status=500
            )
    except Todo.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Task Does not exist"}, status=404
        )


@login_required(login_url="login")
def display_task(request, id):
    try:
        task = get_object_or_404(Todo, id=id)
        if request.method == "GET":
            data = {
                "task_id": task.id,
                "title": task.title,
                "description": task.description,
                "created_at": task.formatted_created_at,
                "time_ago_created_at": task.time_ago_created_at,
                "time_ago_updated_at": task.time_ago_updated_at,
                "updated_at": task.formatted_updated_at,
                "status": task.status,
            }
            return JsonResponse(data, status=200)
    except Todo.DoesNotExist:
        return JsonResponse(
            {"status": "error", "message": "Task does not exist"}, status=404
        )
