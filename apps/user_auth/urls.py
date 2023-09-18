from django.urls import path

from .views import login_view, signup, logout_view

app_name = "auth"

urlpatterns = [
    path(route="sign-up/", view=signup, name="sign_up"),
    path(route="login/", view=login_view, name="login"),
    path(route="logout/", view=logout_view, name="logout"),
]
