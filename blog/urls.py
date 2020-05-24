"""
    Defines the URL patterns for the blog app.
"""
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),

    # Blog page listing article snippets.
    path('blog/', views.blog, name='blog'),

    # Blog detail view - shows the full article detail.
    path('blog/article/<slug:slug>', views.article_detail, name='article_detail'),

    # Articles created by the current user only.
    path('blog/my-articles', views.user_articles, name='user_articles'),

    # Add new article
    path('blog/add-article', views.add_article, name='add_article'),

    # Edit article
    path('blog/edit-article/<slug:slug>', views.edit_article, name='edit_article'),

    # Delete article
    path('blog/delete-article/<slug:slug>', views.delete_article, name='delete_article')
]
