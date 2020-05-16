from django.shortcuts import render, get_object_or_404
from .models import Article
# Create your views here.

def article_list(request):
    articles = Article.active.all()
    return render(request, 'blogapp/article/index.html', {'articles': articles})

def article_full(request, article):
    article = get_object_or_404(Article,slug=article)
    print(article)
    return render(request,'blogapp/article/detail.html', {'article': article})