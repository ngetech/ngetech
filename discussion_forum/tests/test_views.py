from django.test import TestCase, Client
from django.urls import reverse
from discussion_forum.views import *
from django.contrib.auth.models import User

# Create your tests here.
class TestViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="dummy", password="dummy")
        discussion = ForumDiscussion.objects.create(title="Dummy Discussion", content="Dummy Content", user=user)
        reply = ForumReply.objects.create(content="Dummy Reply", user=user, discussion=discussion)
        ForumReply.objects.create(content="Dummy Nested Reply", user=user, reply=reply, replying_to="dummy")

    # --------------- discussion_forum:discussion ---------------
    def test_discussion_views(self):
        client = Client()
        res = client.get(reverse("discussion_forum:discussion"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "forum.html")

    # --------------- discussion_forum:create-discussion ---------------
    def test_create_discussion_views(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.get(reverse("discussion_forum:create-discussion"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "create_discussion.html")

    def test_create_discussion_views_not_logged_in(self):
        client = Client()
        res = client.get(reverse("discussion_forum:create-discussion"))
        self.assertEqual(res.status_code, 302)

    # --------------- discussion_forum:post-discussion ---------------
    def test_post_discussion_views(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:post-discussion"), {"title": "dummy", "content": "dummy"})
        self.assertEqual(res.status_code, 200)
        
    def test_post_discussion_views_not_logged_in(self):
        client = Client()
        res = client.get(reverse("discussion_forum:post-discussion"))
        self.assertEqual(res.status_code, 302)

    def test_post_discussion_views_bad_request(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:post-discussion"), {"title": "dummy"})
        self.assertEqual(res.status_code, 400)
        res = client.post(reverse("discussion_forum:post-discussion"), {"content": "dummy"})
        self.assertEqual(res.status_code, 400)
        res = client.post(reverse("discussion_forum:post-discussion"))
        self.assertEqual(res.status_code, 400)
        res = client.get(reverse("discussion_forum:post-discussion"))
        self.assertEqual(res.status_code, 400)

    # --------------- discussion_forum:get-discussions ---------------
    def test_get_discussions_views(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-discussions"))
        self.assertEqual(res.status_code, 200)

    # --------------- discussion_forum:get-discussion-by-id ---------------
    def test_get_discussion_by_id_views(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-discussion-by-id", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "discussion.html")

    def test_get_discussion_by_id_views_not_found(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-discussion-by-id", kwargs={"id": 100}))
        self.assertEqual(res.status_code, 404)

    # --------------- discussion_forum:get-discussion-replies ---------------
    def test_get_discussion_replies_views(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-discussion-replies", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 200)

    def test_get_discussion_replies_views_not_found(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-discussion-replies", kwargs={"id": 100}))
        self.assertEqual(res.status_code, 404)

    # --------------- discussion_forum:add-discussion-reply ---------------
    def test_add_discussion_reply_views(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:add-discussion-reply", kwargs={"id": 1}), {"content": "dummy"})
        self.assertEqual(res.status_code, 200)
    
    def test_add_discussion_reply_views_not_logged_in(self):
        client = Client()
        res = client.get(reverse("discussion_forum:add-discussion-reply", kwargs={"id": 1}), {"content": "dummy"})
        self.assertEqual(res.status_code, 302)

    def test_add_discussion_reply_views_bad_request(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:add-discussion-reply", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 400)
        res = client.get(reverse("discussion_forum:add-discussion-reply", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 400)

    def test_add_discussion_reply_views_not_found(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:add-discussion-reply", kwargs={"id": 100}), {"content": "dummy"})
        self.assertEqual(res.status_code, 404)

    # --------------- discussion_forum:add-nested-reply ---------------
    def test_add_nested_reply_views(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:add-nested-reply", kwargs={"id": 1}), {"content": "dummy", "user": "dummy"})
        self.assertEqual(res.status_code, 200)

    def test_add_nested_reply_views_not_logged_in(self):
        client = Client()
        res = client.post(reverse("discussion_forum:add-nested-reply", kwargs={"id": 1}), {"content": "dummy", "user": "dummy"})
        self.assertEqual(res.status_code, 302)

    def test_add_nested_reply_views_bad_request(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:add-nested-reply", kwargs={"id": 1}), {"user": "dummy"})
        self.assertEqual(res.status_code, 400)
        res = client.post(reverse("discussion_forum:add-nested-reply", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 400)
        res = client.get(reverse("discussion_forum:add-nested-reply", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 400)

    def test_add_nested_reply_views_not_found(self):
        client = Client()
        client.login(username="dummy", password="dummy")
        res = client.post(reverse("discussion_forum:add-nested-reply", kwargs={"id": 100}), {"content": "dummy"})
        self.assertEqual(res.status_code, 404)

    # --------------- discussion_forum:get-nested-replies ---------------
    def test_get_nested_replies_views(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-nested-replies", kwargs={"id": 1}))
        self.assertEqual(res.status_code, 200)

    def test_get_nested_replies_views_not_found(self):
        client = Client()
        res = client.get(reverse("discussion_forum:get-nested-replies", kwargs={"id": 100}))
        self.assertEqual(res.status_code, 404)