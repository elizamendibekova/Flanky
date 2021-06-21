import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Post
from django.urls import reverse

# Create your tests here.
def create_post(body, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Post.objects.create(body=body, pub_date=time)

class PostModelTests(TestCase):
    def test_was_published_recently_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(pub_date=time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_post = Post(pub_date=time)
        self.assertIs(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_post = Post(pub_date=time)
        self.assertIs(recent_post.was_published_recently(), True)

class PostDetailViewTests(TestCase):
    def test_future_post(self):
        future_post = create_post(body='Future post.', days=5)
        url = reverse('BlogApp:detail', args=(future_post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_post(self):
        past_post = create_post(body='Past post.', days=-5)
        url = reverse('BlogApp:detail', args=(past_post.id,))
        response = self.client.get(url)
        self.assertContains(response, past_post.body)

class PostDetailViewTests(TestCase):
    def test_future_post(self):
        future_post = create_post(body='Future post.', days=5)
        url = reverse('BlogApp:detail', args=(future_post.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_post(self):
        past_post = create_post(body='Past post.', days=-5)
        url = reverse('BlogApp:detail', args=(past_post.id,))
        response = self.client.get(url)
        self.assertContains(response, past_post.body)