from django.test import TestCase
from django.urls import reverse, resolve
from discussion_forum.views import *

# Create your tests here.
class TestUrls(TestCase):
    def test_discussion_url(self):
        url = reverse("discussion_forum:discussion")
        self.assertEqual(resolve(url).func, discussion)

    def test_create_discussion_url(self):
        url = reverse("discussion_forum:create-discussion")
        self.assertEqual(resolve(url).func, create_discussion)

    def test_post_discussion_url(self):
        url = reverse("discussion_forum:post-discussion")
        self.assertEqual(resolve(url).func, post_discussion)

    def test_get_discussion_by_id_url(self):
        url = reverse("discussion_forum:get-discussion-by-id", kwargs={"id": 1})
        self.assertEqual(resolve(url).func, get_discussion_by_id)

    def test_get_discussion_replies_url(self):
        url = reverse("discussion_forum:get-discussion-replies", kwargs={"id": 1})
        self.assertEqual(resolve(url).func, get_discussion_replies)

    def test_add_discussion_reply_url(self):
        url = reverse("discussion_forum:add-discussion-reply", kwargs={"id": 1})
        self.assertEqual(resolve(url).func, add_discussion_reply)

    def test_add_nested_reply_url(self):
        url = reverse("discussion_forum:add-nested-reply", kwargs={"id": 1})
        self.assertEqual(resolve(url).func, add_nested_reply)

    def test_get_nested_replies_url(self):
        url = reverse("discussion_forum:get-nested-replies", kwargs={"id": 1})
        self.assertEqual(resolve(url).func, get_nested_replies)