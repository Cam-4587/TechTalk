from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CommentForm, CreateBlogPost, ReplyForm
from .models import Post, Comment

# Create your tests here.

# Forms Testing


class TestCommentForm(TestCase):
    """Test for comment form validation"""

    def test_form_is_valid(self):
        """Test that the comment form is valid when content is provided"""
        comment_form = CommentForm({
            'content': 'This is a comment to the post'
        })
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        """Test that the comment form is invalid when content is empty"""
        comment_form = CommentForm({'content': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")


class TestReplyForm(TestCase):
    """Test for reply form validation"""

    def test_form_is_valid(self):
        """Test that the reply form is valid when content is provided"""
        reply_form = ReplyForm({'content': 'This is a reply to the comment.'})
        self.assertTrue(reply_form.is_valid())

    def test_form_is_invalid(self):
        """Test that the reply form is invalid when content is empty"""
        reply_form = ReplyForm({'content': ''})
        self.assertFalse(reply_form.is_valid(), msg="Form is valid")


# View Testing


class TestBlogViews(TestCase):
    """Tests for blog views"""

    def setUp(self):
        """Set up a superuser and a blog post for the tests"""
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.client.login(username="myUsername", password="myPassword")
        self.post = Post(
            title="Blog title",
            author=self.user,
            slug="blog-title",
            content="Blog content",
            status=1
        )
        self.post.save()

    def test_render_post_blog_page(self):
        """Test that the blog post page is rendered correctly"""
        response = self.client.get(reverse('post_blog', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"blog-title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertTemplateUsed(response, "blog/post_blog.html")
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        self.assertIsInstance(response.context['reply_form'], ReplyForm)

    def test_successful_comment_submission(self):
        """Test that a comment can be successfully submitted to a blog post"""
        post = Post.objects.create(
            title="Blog Title",
            content='This is a test comment.',
            author=self.user
        )
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'content': 'This is a test comment.'}
        response = self.client.post(
            reverse('comment-sent', args=['blog-title']), post_data
        )
        self.assertRedirects(response, "/blog-title/", 302)

    def test_successful_reply_submission(self):
        """Test that a reply can be successfully submitted to a comment"""
        comment = Comment.objects.create(
            post=self.post,
            content='This is a test comment.',
            author=self.user
        )
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'content': 'This is a test Reply.'}
        response = self.client.post(reverse(
            'reply-sent', args=[comment.pk]), post_data)
        self.assertRedirects(response, "/blog-title/", 302)
