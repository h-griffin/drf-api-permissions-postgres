from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Book

class BooksModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Book.objects.create(
            title = 'Title of Book',
            author = test_user,
            description = 'Words about the book'
        )
        test_post.save()

    def test_blog_content(self):
        book = Book.objects.get(id=1)

        self.assertEqual(book.title, 'Title of Book')
        self.assertEqual(str(book.author), 'tester')
        self.assertEqual(book.description, 'Words about the book')
        