from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def signup(request):
    context = {}
    return render(request=request, template_name="pages/auth/signup.html", context=context)


def login_view(request):
    context = {
        "alert": "hidden",
        "msg": "",
    }
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

    return render(request=request, template_name="pages/auth/login.html", context=context)


def logout_view(request):
    logout(request=request)
    return redirect(to="auth:login")
