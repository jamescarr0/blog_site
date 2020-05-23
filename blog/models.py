from django.db import models
from django.urls import reverse


class Article(models.Model):
    """
    A class to represent users articles.

    Attributes
    ----------
    self.title : str
        title of users article.
    self.body : str
        article/blog content.
    self.date : date
        time and date of article submission.
    self.slug : str
        Pretty URL slugs for blog pages.

    Methods
    -------
    ___str___():
        returns a string representation of the model.

    snippet():
        returns a string snippet with ellipsis.

    get_absolute_url():
        returns a URL using a 'slug' as its key
    """

    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        """ Returns a string representation of the model. """
        return self.title

    def snippet(self):
        """ Return a string snippet plus ellipsis. """
        snippet = f"{self.body[:50]}..."
        return snippet

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})
