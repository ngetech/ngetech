from django.test import TestCase
from discussion_forum.models import *
from django.contrib.auth.models import User

# Create your tests here.
class TestModels(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="dummy", password="dummy")
        discussion = ForumDiscussion.objects.create(title="Dummy Discussion", content="Dummy Content", user=user)
        reply = ForumReply.objects.create(content="Dummy Reply", user=user, discussion=discussion)
        ForumReply.objects.create(content="Dummy Nested Reply", user=user, reply=reply, replying_to="dummy")
    
    def test_discussion_models(self):
        user = User.objects.get(username="dummy")
        discussion = ForumDiscussion.objects.get(pk=1)
        self.assertEqual(discussion.title, "Dummy Discussion")
        self.assertEqual(discussion.content, "Dummy Content")
        self.assertEqual(discussion.user, user)

    def test_reply_models(self):
        user = User.objects.get(username="dummy")
        discussion = ForumDiscussion.objects.get(pk=1)
        reply = ForumReply.objects.get(discussion=discussion)
        self.assertEqual(reply.content, "Dummy Reply")
        self.assertEqual(reply.discussion, discussion)
        self.assertEqual(reply.user, user)

    def test_nested_reply_models(self):
        user = User.objects.get(username="dummy")
        discussion = ForumDiscussion.objects.get(pk=1)
        reply = ForumReply.objects.get(discussion=discussion)
        nested_reply = ForumReply.objects.get(reply=reply)
        self.assertEqual(nested_reply.content, "Dummy Nested Reply")
        self.assertEqual(nested_reply.reply, reply)
        self.assertEqual(nested_reply.user, user)