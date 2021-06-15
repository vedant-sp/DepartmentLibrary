from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.db.utils import IntegrityError


# Create your views here.
def login(request):
    return render(request, "login.html")


def files(request):
    return render(request, "files.html")


def ongoing(request):
    return render(request, "ongoing.html")


def history(request):
    return render(request, "history.html")


def validate(request):
    username = request.POST["username"]
    password = request.POST["pass"]

    user = authenticate(username=username, password=password)
    if user is not None:
        return render(request, "index.html")
    else:
        return render(request, "login1.html")


def index(request):
    return render(request, "index.html")


def logout_request(request):
    messages.info(request, "Logged out successfully!")
    return render(request, "login.html")


def user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = email.split("@")[0]
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password1)
        user.save();
        try:
            print('user created')
            return render(request, 'login.html')
        except IntegrityError as e:
            e = 'this data already exists in the database'
            return render(request, "register.html", context={'e': e})

    else:
        return render(request, 'register.html')


def signup(request):
    return render(request, 'register.html')
