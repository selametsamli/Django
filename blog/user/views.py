from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.

def register(request):
    form = RegisterForm()
    contex ={
        "form": form
    }

    return render(request,"register.html",contex)


def loginUser(request):
    return render(request,"login.html")


def logoutUser(request):
    pass
