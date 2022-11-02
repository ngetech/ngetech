import datetime
import json
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from tech_survey.models import HasilTechSurvey
from tech_survey.forms import TechSurveyForm
from tech_survey.views import show_tech_survey, get_result_json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='userdummy', password='123')
        self.survey_url = reverse('tech_survey:show-tech-survey')
        self.get_json_url = reverse('tech_survey:result-json')
    
    # ----------- Show Views for Non Logged in Users -----------
    def test_show_tech_survey_GET(self):
        response = self.client.get(self.survey_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tech_survey.html')

    def test_result_json_GET(self):
        response = self.client.get(self.get_json_url)
        self.assertEquals(response.status_code, 302)
    
    # ----------- Show Views for Logged in Users -----------
    def test_show_tech_survey_logged_in(self):
        self.client.login(username='userdummy', password='123')
        self.hasil1 = HasilTechSurvey.objects.create(owner=self.user, result='Sobat Ngetech abiez!')
        res = self.client.get(self.survey_url, {'form':TechSurveyForm(), 'riwayat':self.hasil1})
        self.assertEqual(res.status_code, 200)

    def test_result_json_logged_in(self):
        self.client.login(username='userdummy', password='123')
        self.hasil1 = HasilTechSurvey.objects.create(owner=self.user, result='Sobat Ngetech abiez!')
        res = self.client.post(self.get_json_url, {'result': self.hasil1})
        self.assertEqual(res.status_code, 200)

    # ----------- Test Result (1st survey) for Logged in Users -----------
    def test_result_first_survey(self):
        self.client.login(username='userdummy', password='123')
        form_data = {
            'que_1': '3',
            'que_2': '3',
            'que_3': '3',
            'que_4': '3',
            'que_5': '3',
            'que_6': '3',
            'que_7': '3',
            'que_8': '3',
        }
        res = self.client.post(self.get_json_url, data=form_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], 'Sobat Ngetech abiez!')

    # ----------- Test Result (2st survey) for Logged in Users -----------
    def test_result_second_survey(self):
        self.client.login(username='userdummy', password='123')
        self.hasil1 = HasilTechSurvey.objects.create(owner=self.user, result='Sobat Ngetech abiez!')
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
        res = self.client.post(self.get_json_url, data=form_data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], 'Kurang ngetech')
    
    # ----------- Test Result 1 to 5 for Logged in Users -----------
    def test_result_1(self):
        self.client.login(username='userdummy', password='123')
        form_data = {
            'que_1': '3',
            'que_2': '3',
            'que_3': '3',
            'que_4': '3',
            'que_5': '3',
            'que_6': '3',
            'que_7': '3',
            'que_8': '3',
        }
        res = self.client.post(self.get_json_url, data=form_data)
        self.hasil1 = HasilTechSurvey.objects.create(owner=self.user, result='Sobat Ngetech abiez!')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], self.hasil1.result)
    
    def test_result_2(self):
        self.client.login(username='userdummy', password='123')
        form_data = {
            'que_1': '2',
            'que_2': '2',
            'que_3': '2',
            'que_4': '2',
            'que_5': '2',
            'que_6': '2',
            'que_7': '2',
            'que_8': '1',
        }
        res = self.client.post(self.get_json_url, data=form_data)
        hasil2 = HasilTechSurvey.objects.create(owner=self.user, result='Tech enthusiasts')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], hasil2.result)

    def test_result_3(self):
        self.client.login(username='userdummy', password='123')
        form_data = {
            'que_1': '2',
            'que_2': '2',
            'que_3': '1',
            'que_4': '1',
            'que_5': '1',
            'que_6': '1',
            'que_7': '1',
            'que_8': '1',
        }
        res = self.client.post(self.get_json_url, data=form_data)
        hasil3 = HasilTechSurvey.objects.create(owner=self.user, result='Great start!')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], hasil3.result)

    def test_result_4(self):
        self.client.login(username='userdummy', password='123')
        form_data = {
            'que_1': '1',
            'que_2': '1',
            'que_3': '1',
            'que_4': '1',
            'que_5': '1',
            'que_6': '0',
            'que_7': '0',
            'que_8': '0',
        }
        res = self.client.post(self.get_json_url, data=form_data)
        hasil4 = HasilTechSurvey.objects.create(owner=self.user, result='Ngetech lagi yuk!')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], hasil4.result)
    
    def test_result_5(self):
        self.client.login(username='userdummy', password='123')
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
        res = self.client.post(self.get_json_url, data=form_data)
        hasil5 = HasilTechSurvey.objects.create(owner=self.user, result='Kurang ngetech')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content)['result'], hasil5.result)
        