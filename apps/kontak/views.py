from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import redirect, render

from .forms.kontak import Kontak as KontakForm
from .models.kontak import Kontak as KontakModel


@login_required(login_url="auth:login")
def index(request):
    model = KontakModel.objects.all().order_by("-id")
    page = request.GET.get("page", 1)

    paginator = Paginator(object_list=model, per_page=5)

    try:
        data = paginator.page(number=page)
    except PageNotAnInteger:
        data = paginator.page(number=1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    print("\n\n", data, "\n\n")
    # data = paginator

    context = {"data": data}

    return render(request=request, template_name="kontak/index.html", context=context)


@login_required(login_url="auth:login")
def add(request):
    data = KontakForm(request.POST or None)

    if request.method == "POST":
        if data.is_valid():
            data.save()
            return redirect(to="kontak:index")

    context = {"data": data}

    return render(request=request, template_name="kontak/add.html", context=context)


@login_required(login_url="auth:login")
def detail(request, id):
    data = KontakModel.objects.get(id=id)

    context = {"data": data}

    return render(request=request, template_name="kontak/detail.html", context=context)


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

    return render(request=request, template_name="kontak/edit.html", context=context)


@login_required(login_url="auth:login")
def detele(request, id):
    KontakModel.objects.filter(id=id).delete()
    return redirect(to="kontak:index")
