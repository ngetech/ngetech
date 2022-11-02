from django.test import TestCase, Client
from tech_survey.forms import TechSurveyForm
from tech_survey.models import HasilTechSurvey

class TestForms(TestCase):
    def test_forms_is_valid(self):
        form_data = {
            'que_1': '0',
            'que_2': '0',
            'que_3': '0',
            'que_4': '0',
            'que_5': '0',
            'que_6': '0',
            'que_7': '0',
            'que_8': '0',
        }
        form = TechSurveyForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_forms_is_not_valid(self):
        form_data = {'que_1': '0'}
        form = TechSurveyForm(data=form_data)
        self.assertFalse(form.is_valid())