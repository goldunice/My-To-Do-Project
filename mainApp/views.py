from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Plan.objects.create(
                title=request.POST.get("name"),
                details=request.POST.get("details"),
                date=request.POST.get("date"),
                status=request.POST.get("status"),
                egasi=Talaba.objects.filter(user=request.user).first()
            )
            return redirect("/home/")

        holat = [x[0] for x in status]
        talaba = Talaba.objects.filter(user=request.user).first()
        content = {
            "holatlar": holat,
            "rejalar": Plan.objects.filter(egasi=talaba),
            "foydalanuvchi": request.user.username.capitalize()
        }
        return render(request, 'index.html', content)
    else:
        return redirect("/")


def delete_plan(request, num):
    if request.user.is_authenticated:
        Plan.objects.get(id=num).delete()
        return redirect("/home/")
    return redirect('/')


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
    context = {
        "reja": Plan.objects.get(id=num),
        "holatlar": holat
    }
    return render(request, 'edit.html', context)


def login_view(request):
    if request.method == 'POST' and request.POST.get("forma") == "f2":
        user = authenticate(
            username=request.POST.get("l"),
            password=request.POST.get("p")
        )
        if user is None:
            return redirect("/")
        login(request, user)
        return redirect("/home/")
    elif request.method == 'POST' and request.POST.get("forma") == "f1":
        try:
            User.objects.create_user(
                username=request.POST.get("l"),
                email=request.POST.get("email"),
                password=request.POST.get("p1"),
            )
        finally:
            return redirect("/")

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect("/")
