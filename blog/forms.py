"""
    Using ModelForm to automatically build a form using the information
    from the models defined in models.py
"""

from django import forms

from .models import Article


class AddArticleForm(forms.ModelForm):
    """ Automatically build a form using the information from supplied model. """

    class Meta:
        model = Article
        fields = ['title', 'body', 'slug']
        labels = {'slug': 'SEO URL Slug'}


class EditArticleForm(AddArticleForm):
    """ Automatically build a form using the information from the supplied model. """
