import os
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    """
    A class to represent users articles.

    Attributes
    ----------
    title : str
        title of users article.
    body : str
        article/blog content.
    date : date
        time and date of article submission.
    slug : str
        Pretty URL slugs for blog pages.
    author : user
        name of the user who created the article.

    Methods
    -------
    create_path:
        returns a path to the users media directory.
        
    ___str___():
        returns a string representation of the model.

    snippet():
        returns a string snippet with ellipsis.

    get_absolute_url():
        returns a URL using a 'slug' as its key
    """

    def create_path(instance, filename):
        """ Returns the users media directory.  """
        path = os.path.join('users/' + instance.author.username, 'images/', filename)
        return path

    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=create_path, blank=True)

    def __str__(self):
        """ Returns a string representation of the model. """
        return self.title

    def snippet(self):
        """ Return a string snippet plus ellipsis. """
        snippet = f"{self.body[:150]}..."
        return snippet

    def get_absolute_url(self):
        """ returns the URL for the requested article. """
        return reverse('blog:article_detail', kwargs={'slug': self.slug})
