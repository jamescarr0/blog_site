import os
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
    self.author : user
        name of the user who created the article.
    self.image : ImageField
        Image uploaded by user.
    self.image_alt : str
        Image ALT tag for HTML templates.


    Methods
    -------
    create_path:
        returns a path to the users media directory.

    _create_img_filename:
        returns a new image filename before saving relating to its content.

    ___str___():
        returns a string representation of the model.

    snippet():
        returns a string snippet with ellipsis.

    get_absolute_url():
        returns a URL using a 'slug' as its key
    """

    def create_path(instance, filename):
        """ Returns the path to save users image.  """

        # Rename image filename.
        filename = instance._create_img_filename(filename)

        # Create path to image.
        path = os.path.join('users/' + instance.author.username, 'images/', filename)
        return path

    def _create_img_filename(self, filename):
        """ Rename the uploaded image relating to the content.
            Returns the new filename.
        """
        # Get the image extension
        ext = filename.split('.')[-1]

        # Create filename base on the slug and add the extension.
        filename = f'{self.slug}.{ext}'
        return filename

    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=create_path, blank=True)
    image_alt = models.CharField(max_length=125)

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
