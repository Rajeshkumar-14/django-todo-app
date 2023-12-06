from django.urls import path
from . import views

__project_by__ = "RajeshKumar"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("logout/", views.user_logout, name="logout"),
    path("reset-password/", views.reset_password, name="reset-password"),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        views.reset_confirm,
        name="passwordresetconfirm",
    ),
]
