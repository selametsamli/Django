from django.shortcuts import render, HttpResponse
from .forms import ArticleForm

# Create your views here.

def index(request):

    context ={
        "numbers":[1,2,3,4,5,6]

    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def dashboard(request):
    return render(request,"dashboard.html")


def addarticle(request):
    form = ArticleForm()

    return render(request,"addarticle.html",{"form":form})