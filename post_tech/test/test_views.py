from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
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

    def test_get_tech_post_response(self):
        response = self.client.get(
            self.url_to_get_json
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_add_post_tech_response(self):
        response = self.client.get(
            self.url_to_add_post_tech
        )
        self.assertEqual(
            response.status_code,
            302
        )

    def test_add_likes_response(self):
        response = self.client.get(
            self.url_to_like_post
        )
        self.assertEqual(
            response.status_code,
            302
        )
