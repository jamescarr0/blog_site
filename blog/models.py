from django.db import models


class Blog(models.Model):
    """
    A class to represent a users blog articles.

    Attributes
    ----------
    self.title : str
        title of users blog.
    self.body : str
        article/blog content.
    self.date : date
        time and date of article submission.
    self.slug : str

    Methods
    -------
    ___str___():
        returns a string represenation of the model.
    snippet():
        returns a string snippet with ellipsis.
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
