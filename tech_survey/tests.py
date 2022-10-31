from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .forms import TechSurveyForm
from .views import show_tech_survey, get_result_json
from .models import HasilTechSurvey

class TechSurveyTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='userdummy', password='123')
        hasil = HasilTechSurvey.objects.create(owner=user, result='Sobat Ngetech abiez!')

    # Model test
    def test_create_model(self):
        user = User.objects.get(username="userdummy")
        hasil = HasilTechSurvey.objects.get(pk=1)
        self.assertEqual(hasil.owner, user)
        self.assertEqual(hasil.result, 'Sobat Ngetech abiez!')

    # Test if URL can shows Views correctly
    def test_show_tech_survey(self):
        link = reverse('tech_survey:show-tech-survey')
        self.assertEqual(resolve(link).func, show_tech_survey)
    
    def test_get_result_json(self):
        link = reverse('tech_survey:result-json')
        self.assertEqual(resolve(link).func, get_result_json)
        
