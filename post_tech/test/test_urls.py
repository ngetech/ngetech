from django.test import TestCase
from django.urls import reverse, resolve
from post_tech.urls import *

class TestUrls(TestCase):

    def setUp(self):
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

    def test_url_to_main_view(self):
        self.assertEqual(
            resolve(
                self.url_to_main_view
            ).func,
            show_post_tech
        )

    def test_url_to_get_json(self):
        self.assertEqual(
            resolve(
                self.url_to_get_json
            ).func,
            get_tech_post
        )

    def test_url_to_add_post_tech(self):
        self.assertEqual(
            resolve(
                self.url_to_add_post_tech
            ).func,
            add_post_tech
        )

    def test_url_to_like_post(self):
        self.assertEqual(
            resolve(
                self.url_to_like_post
            ).func,
            add_likes
        )
