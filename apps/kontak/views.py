from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms.kontak import Kontak as KontakForm
from .models.kontak import Kontak as KontakModel


@login_required(login_url="auth:login")
def index(request):
    datas = KontakModel.objects.all()

    context = {
        "datas": datas,
    }

    return render(request=request, template_name="pages/kontak/index.html", context=context)


@login_required(login_url="auth:login")
def add(request):
    data = KontakModel()

    context = {
        "form": "Add",
        "data": data,
        "gender": KontakModel.GENDER,
    }

    if request.method == "POST":
        data = KontakModel(
            nama=request.POST["nama"],
            email=request.POST["email"],
            gender=request.POST["gender"],
            phone=request.POST["phone"],
            alamat=request.POST["alamat"]
        )
        data.save()
        return redirect(to="kontak:index")

    # return render(request=request, template_name="pages/kontak/add.html", context=context)
    return render(request=request, template_name="pages/kontak/form.html", context=context)


@login_required(login_url="auth:login")
def detail(request, id):
    data = KontakModel.objects.get(id=id)

    context = {
        "form": "Detail",
        "data": data,
        "gender": KontakModel.GENDER,
        "disabled": "disabled",
        "hidden": "hidden"
    }

    # return render(request=request, template_name="pages/kontak/detail.html", context=context)
    return render(request=request, template_name="pages/kontak/form.html", context=context)


@login_required(login_url="auth:login")
def edit(request, id):
    data = KontakModel.objects.get(id=id)

    data.nama = request.POST["nama"] if request.method == "POST" else data.nama
    data.email = request.POST["email"] if request.method == "POST" else data.email
    data.gender = request.POST["gender"] if request.method == "POST" else data.gender
    data.phone = request.POST["phone"] if request.method == "POST" else data.phone
    data.alamat = request.POST["alamat"] if request.method == "POST" else data.alamat

    if request.method == "POST":
        data.save()
        return redirect(to="kontak:index")

    context = {
        "form": "Edit",
        "data": data,
        "gender": KontakModel.GENDER,
    }

    # return render(request=request, template_name="pages/kontak/add_edit_lab.html", context=context)
    return render(request=request, template_name="pages/kontak/form.html", context=context)


@login_required(login_url="auth:login")
def detele(request, id):
    KontakModel.objects.filter(id=id).delete()
    return redirect(to="kontak:index")
