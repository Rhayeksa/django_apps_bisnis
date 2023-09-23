from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def signup(request):
    context = {"alert": "hidden"}
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        check_username = User.objects.filter(username=username).exists()
        check_email = User.objects.filter(email=email).exists()
        if check_username:
            context = {
                "alert": "",
                "msg": "Username sudah terdaftar"
            }
        elif check_email:
            context = {
                "alert": "",
                "msg": "Email sudah terdaftar"
            }
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect(to="auth:login")
    return render(request=request, template_name="user_auth/signup.html", context=context)


def login_view(request):
    context = {"alert": "hidden"}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request=request, user=user)
            return redirect(to="index")
        else:
            context = {
                "alert": "",
                "msg": "username atau password salah",
            }

    return render(request=request, template_name="user_auth/login.html", context=context)


def logout_view(request):
    logout(request=request)
    return redirect(to="auth:login")
