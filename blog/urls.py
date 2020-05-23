"""
    Defines the URL patterns for the blog app.
"""
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blog/article/<slug:slug>', views.article_detail, name='article_detail'),
]
