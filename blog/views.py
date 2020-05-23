from django.shortcuts import render, redirect

from .models import Article
from .forms import AddArticleForm, EditArticleForm


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
    """ Show the full article. """
    article = Article.objects.get(slug=slug)
    context = {'article': article}
    return render(request, 'article_detail.html', context)


def add_article(request):
    """ Add a new article. """
    if request.method != 'POST':
        # No data submitted, create a blank form.
        form = AddArticleForm()
    else:
        # POST data submitted, process data.
        form = AddArticleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return back_to_blog_page()

    context = {'form': form}
    return render(request, 'add_article.html', context)


def edit_article(request, slug):
    """ Edit an existing article. """
    article = Article.objects.get(slug=slug)

    if request.method != 'POST':
        # Initial request pre-populate form with current article content.
        form = EditArticleForm(instance=article)
    else:
        # POST data submitted, process data.
        form = EditArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return back_to_blog_page()

    context = {'article': article, 'form': form}
    return render(request, 'edit_article.html', context)


def delete_article(request, slug):
    """ Delete an existing article. """
    article = Article.objects.get(slug=slug)
    article.delete()
    return back_to_blog_page()


def back_to_blog_page():
    """ returns the appropriate url the arguments passed. """
    return redirect('blog:blog')
