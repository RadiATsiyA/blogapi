from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser = User.objects.create_user(
            username="testuser",
            email="test@gmail.com",
            password="pass123"
        )
        testuser.save()

        test_post = Post.objects.create(
            author=testuser,
            title="TestBlog",
            body="test body text"
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"

        self.assertEqual(author, "testuser")
        self.assertEqual(title, "TestBlog")
        self.assertEqual(body, "test body text")
