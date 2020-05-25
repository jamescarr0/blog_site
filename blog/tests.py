import datetime
from django.test import TestCase
from blog.models import Article
from django.contrib.auth.models import User


class BlogTests(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            author=User.objects.create_user(username='test-user', password='password'),
            title='Article Testing Title',
            body='Article body contains user content',
            date=datetime.date(2020, 1, 1),
            slug='article-testing',
            image='ishdfkj98w3r.jpg',
            image_alt='image alt'
        )
        self.client.login(username='test-user', password='password')
        self.user = User.objects.get(username='test-user')

    def test_create_img_filename(self):
        """ Test that the uploaded image filename is renamed relevant to content. """
        original_filename = self.article.image.name
        new_filename = self.article._create_img_filename(original_filename)
        self.assertEqual(new_filename, 'article-testing.jpg')

    def test_create_path(self):
        """
        Test that the image is saved into a user directory
        'users/{username}/images/{image}'
        """
        path = self.article.create_path(self.article.image.name)
        self.assertEqual(path, f'users/{self.user.username}/images/article-testing.jpg')

    def test_snippet(self):
        """ Test that snippet length does not exceed 150 characters. """
        snippet = self.article.snippet()
        self.assertTrue(len(snippet) < 150)
