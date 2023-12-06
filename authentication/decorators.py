from django.shortcuts import redirect
from django.contrib import messages


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            return redirect("index")
        return view_func(request, *args, **kwargs)

    return wrapper_func
