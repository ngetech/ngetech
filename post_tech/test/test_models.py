from turtle import title
from django.test import TestCase
from django.contrib.auth.models import User
from post_tech.models import PostTech

class TestModels(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username= 'user.testing',
            password= 'testing1234'
        )
        self.post_tech = PostTech.objects.create(
            user=self.user,
            username=self.user.username,
            title='Post Title',
            description="""
                Contrary to popular belief, Lorem Ipsum is not simply random text. 
                It has roots in a piece of classical Latin literature from 45 BC, 
                making it over 2000 years old. Richard McClintock, a Latin professor 
                at Hampden-Sydney College in Virginia, looked up one of the more obscure 
                Latin words, consectetur, from a Lorem Ipsum passage, and going through 
                the cites of the word in classical literature, discovered the undoubtable 
                source.
            """
        )

    def test_create_post(self):
        self.assertEqual(
            self.post_tech,
            PostTech.objects.get(
                user=self.user,
                title='Post Title'
            )
        )