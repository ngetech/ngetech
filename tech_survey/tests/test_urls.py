from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tech_survey.views import show_tech_survey, get_result_json

class TestUrls(SimpleTestCase):
    def test_tech_survey_url_is_resolved(self):
        link = reverse('tech_survey:show-tech-survey')
        self.assertEqual(resolve(link).func, show_tech_survey)

    def test_resurlt_json_url_is_resolved(self):
        link = reverse('tech_survey:result-json')
        self.assertEqual(resolve(link).func, get_result_json)
