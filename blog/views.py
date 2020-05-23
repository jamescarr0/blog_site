from django.shortcuts import render

from .models import Article


def index(request):
    """ The home page for users blog articles. """
    return render(request, 'index.html')


def blog(request):
    """ Show a snippet of all blog articles. """
    # Get all articles and sort by date added.
    articles = Article.objects.order_by('date')
    context = {'articles': articles}
    return render(request, 'blog.html', context)


def article_detail(request, slug):
    """ Show the full article in detail. """
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_detail.html', context)
