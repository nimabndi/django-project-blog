from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import CreateArticle


def articles_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url='/accounts/login')
def create_article(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = CreateArticle()
    return render(request, 'articles/create_article.html', {'form': form})
