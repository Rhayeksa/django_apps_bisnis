from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms.kontak import Kontak as KontakForm
from .models.kontak import Kontak as KontakModel


@login_required(login_url="auth:login")
def index(request):
    data = KontakModel.objects.all()

    context = {"data": data}

    return render(request=request, template_name="pages/kontak/index.html", context=context)


@login_required(login_url="auth:login")
def add(request):
    data = KontakForm(request.POST or None)

    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect(to="kontak:index")

    context = {"data": data}

    return render(request=request, template_name="pages/kontak/add.html", context=context)


@login_required(login_url="auth:login")
def detail(request, id):
    data = KontakModel.objects.get(id=id)

    context = {"data": data}

    return render(request=request, template_name="pages/kontak/detail.html", context=context)


@login_required(login_url="auth:login")
def edit(request, id):
    model = KontakModel.objects.get(id=id)

    initial = {
        "nama": model.nama,
        "email": model.email,
        "gender": model.gender,
        "phone": model.phone,
        "alamat": model.alamat,
    }

    data = KontakForm(
        data=request.POST or None,
        initial=initial,
        instance=model
    )

    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect(to="kontak:detail", id=model.id)

    context = {"data": data}

    return render(request=request, template_name="pages/kontak/edit.html", context=context)


@login_required(login_url="auth:login")
def detele(request, id):
    KontakModel.objects.filter(id=id).delete()
    return redirect(to="kontak:index")
