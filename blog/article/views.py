from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    articles = Article.objects.all()


    return render(request,"articles.html",{"articles":articles})


def index(request):

    context ={
        "numbers":[1,2,3,4,5,6]

    }
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")


@login_required(login_url = "user:login")
def dashboard(request):

    articles = Article.objects.filter(author=request.user)

    context = {
        "articles":articles
    }

    return render(request,"dashboard.html",context)

@login_required(login_url = "user:login")
def addarticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla oluşturuldu.")
        return redirect("article:dashboard")

    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article = Article.objects.filter(id = id).first()
    article = get_object_or_404(Article,id=id)
    
    return render(request,"detail.html",{"article":article})

@login_required(login_url = "user:login")
def update(request,id):

    article = get_object_or_404(Article, id =id)
    form = ArticleForm(request.POST or None , request.FILES or None, instance= article)
    if form.is_valid():
        article = form.save(commit=False)
        
        article.author = request.user
        article.save()

        messages.success(request,"Makale başarıyla güncelledi.")
        return redirect("index")


    return render(request,"update.html",{"form":form})

@login_required(login_url = "user:login" )
def delete(request,id):
    article = get_object_or_404(Article, id =id)
    article.delete()

    messages.success(request,"Makale başarıyla silindi.")
    return redirect("article:dashboard")


