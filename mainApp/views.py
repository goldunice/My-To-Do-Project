from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Plan.objects.create(
                title=request.POST.get("name"),
                details=request.POST.get("details"),
                date=request.POST.get("date"),
                status=request.POST.get("status"),
                egasi=request.user
            )
            return redirect("/home/")

        holat = [x[0] for x in status]
        content = {
            "holatlar": holat,
            "rejalar": Plan.objects.filter(egasi=request.user),
            "foydalanuvchi": request.user.username.capitalize()
        }
        return render(request, 'index.html', content)
    else:
        return redirect("/")


def delete_plan(request, num):
    Plan.objects.get(id=num).delete()
    return redirect("/home/")


def edit(request, num):
    if request.method == 'POST':
        Plan.objects.filter(id=num).update(
            title=request.POST.get("name"),
            date=request.POST.get("date"),
            status=request.POST.get("status"),
            details=request.POST.get("details"),
        )
        return redirect("/home/")
    holat = [x[0] for x in status]
    content = {
        "reja": Plan.objects.get(id=num),
        "holatlar": holat
    }
    return render(request, 'edit.html', content)


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get("l"),
            password=request.POST.get("p")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/home/")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")
