from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from post_tech.views import *

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="user.testing", 
            password="user.testing"
        )
        self.url_to_main_view = reverse(
            'post-tech:show-post-tech'
        )
        self.url_to_get_json = reverse(
            'post-tech:get-tech-post'
        )
        self.url_to_add_post_tech = reverse(
            'post-tech:add-post-tech'
        )
        self.url_to_like_post = reverse(
            'post-tech:like-post',
            args=[0]
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

    # --------------- post-tech:show-post-tech ---------------
    def test_show_post_tech_response(self):
        response = self.client.get(
            self.url_to_main_view
        )
        self.assertEqual(
            response.status_code,
            200
        )
        self.assertTemplateUsed(
            response,
            'post_tech_index.html'
        )

    # --------------- post-tech:get-tech-post ---------------
    def test_get_tech_post_response(self):
        response = self.client.get(
            self.url_to_get_json
        )
        self.assertEqual(
            response.status_code,
            200
        )

    # --------------- post-tech:add-tech-post ---------------
    def test_add_post_tech_response_case_logged_in(self):
        self.client.login(
            username='user.testing',
            password='user.testing'
        )
        response = self.client.post(
            self.url_to_add_post_tech,
            {
                'title': 'add title',
                'description': 'add description'
            }
        )
        self.assertEqual(
            response.status_code,
            200
        )


    def test_add_post_tech_response_case_not_logged_in(self):
        response = self.client.get(
            self.url_to_add_post_tech
        )
        self.assertEqual(
            response.status_code,
            302
        )

    def test_add_post_tech_response_bad_request(self):
        self.client.login(
            username='user.testing',
            password='user.testing'
        )
        response = self.client.post(
            self.url_to_add_post_tech,
            {
                'title': 'title only',
            }
        )
        self.assertEqual(
            response.status_code,
            400
        )
        response = self.client.post(
            reverse('post-tech:add-post-tech'),
            {'description': 'description only'}
        )
        self.assertEqual(
            response.status_code,
            400
        )
        response = self.client.post(
            reverse('post-tech:add-post-tech'),
        )
        self.assertEqual(
            response.status_code,
            400
        )
        response = self.client.get(
            reverse('post-tech:add-post-tech'),
        )
        self.assertEqual(
            response.status_code,
            400
        )

    # --------------- post-tech:like-post-by-id ---------------
    def test_add_like_response_views_case_logged_in(self):
        self.client.login(
            username='user.testing',
            password='user.testing'
        )
        response = self.client.post(
            reverse(
                'post-tech:like-post',
                kwargs={'key': 1}
            ),
            {}
        )
        self.assertEqual(
            response.status_code,
            200
        )
        response = self.client.post(
            reverse(
                'post-tech:like-post',
                kwargs={'key': 1}
            ),
            {}
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_add_like_response_views_case_not_logged_in(self):
        response = self.client.post(
            reverse(
                'post-tech:like-post',
                kwargs={'key': 1}
            ),
            {}
        )
        self.assertEqual(
            response.status_code,
            302
        )

    def test_add_like_response_views_bad_request(self):
        self.client.login(
            username='user.testing',
            password='user.testing'
        )
        response = self.client.get(
            reverse(
                'post-tech:like-post',
                kwargs={'key': 100000}
            ),
            {}
        )
        self.assertEqual(
            response.status_code,
            400
        )

    def test_add_like_response_views_not_found(self):
        self.client.login(
            username='user.testing',
            password='user.testing'
        )
        response = self.client.post(
            reverse(
                'post-tech:like-post',
                kwargs={'key': 100000}
            ),
            {}
        )
        self.assertEqual(
            response.status_code,
            404
        )