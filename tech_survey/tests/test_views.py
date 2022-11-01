from django.test import TestCase, Client
from django.urls import reverse, resolve
from tech_survey.views import show_tech_survey, get_result_json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.survey_url = reverse('tech_survey:show-tech-survey')
        self.get_json_url = reverse('tech_survey:result-json')
    
    def test_show_tech_survey_GET(self):
        response = self.client.get(self.survey_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tech_survey.html')

    def test_result_json_GET(self):
        response = self.client.get(self.get_json_url)
        self.assertEquals(response.status_code, 302)