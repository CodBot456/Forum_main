from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def login_view(request):
    context = {}
    if request.method=="POST":
        nickname=request.POST["nickname"]
        password=request.POST["password"]
        user = authenticate(username=nickname,password=password)
        if user:
            login(request,user)
        else:
            context['error'] = "Пароль или имя пользователя не верны"

    return render(request,"accounts/login.html", context)


def registration_view(request):
    context = {}
    if request.method=="POST":
        nickname=request.POST["nickname"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        if password1 == password2 :
            try:
                User.objects.create_user(username=nickname , password=password1)
            except:
                context['error'] = "Такой пользователь уже есть"
        else:
            context['error'] = "Пароли не совпадают"

    return render(request,"accounts/registration.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))