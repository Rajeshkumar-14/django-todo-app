from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import SetPasswordForm
from .tasks import send_password_reset
from .decorators import unauthenticated_user

__project_by__ = "RajeshKumar"

@unauthenticated_user
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        requested_user = User.objects.filter(username=username).first()

        if requested_user is None:
            messages.error(request, "The User with this Username is Not available.")
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request, "Invalid Password. Please try again.")
    return render(request, "authentication/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


@unauthenticated_user
def user_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        email = request.POST["email"]

        if password != password1:
            messages.error(request, "Passwords do not match")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, "Username is already taken. Please Sign-Up again"
                )
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already in use.")
            else:
                # Create the User object
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                messages.success(
                    request, "Registration successful. You can now log in."
                )
                return redirect("login")
    return render(request, "authentication/login.html")


@unauthenticated_user
def reset_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            send_password_reset(user.pk)
            messages.success(request, "Password reset email sent successfully.")
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist.")

    return render(request, "authentication/reset-email.html")


@unauthenticated_user
def reset_confirm(request, uidb64, token):
    User = get_user_model()

    # Decode the UID
    uid = urlsafe_base64_decode(uidb64).decode()

    try:
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        messages.error(request, "Invalid user. Please try the password reset again.")
        return redirect("login")

    if request.method == "POST":
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        # Check if the passwords match
        if password == password1:
            # Create a form with the user and the provided password
            form = SetPasswordForm(
                user, {"new_password1": password, "new_password2": password1}
            )

            if form.is_valid():
                # Set the user's password
                form.save()
                messages.success(
                    request,
                    "Password reset successful. You can now log in with your new password.",
                )
                return redirect("login")
            else:
                messages.error(
                    request,
                    "Invalid form data. Please correct the errors and try again.",
                )
        else:
            messages.error(
                request, "Passwords do not match. Please enter matching passwords."
            )
    else:
        # If the request method is not POST, render the form for password reset
        form = SetPasswordForm(user)

    context = {"form": form}
    return render(request, "authentication/reset-password.html", context)
