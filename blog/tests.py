from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import tempfile
from .forms import CommentForm, CreateBlogPost, ReplyForm
from .models import Post

# Create your tests here.

# Forms Testing
class TestCommentForm(TestCase):
    def test_form_is_valid(self):
        commentForm = CommentForm({'content': 'This is a comment to the post'})
        self.assertTrue(commentForm.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        commentForm = CommentForm({'content': ''})
        self.assertFalse(commentForm.is_valid(), msg="Form is valid")
class TestReplyForm(TestCase):
    def test_form_is_valid(self):
        replyForm = ReplyForm({'content': 'This is a reply to the comment.'})
        self.assertTrue(replyForm.is_valid())
        
    def test_form_is_invalid(self):
        replyForm = ReplyForm({'content': ''})
        self.assertFalse(replyForm.is_valid(), msg="Form is valid")



