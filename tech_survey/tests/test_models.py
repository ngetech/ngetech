from django.test import TestCase
from django.contrib.auth.models import User
from tech_survey.models import HasilTechSurvey

class TestModels(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='userdummy', password='123')
        hasil = HasilTechSurvey.objects.create(owner=user, result='Sobat Ngetech abiez!')

    def test_create_model(self):
        user = User.objects.get(username="userdummy")
        hasil = HasilTechSurvey.objects.get(pk=1)
        self.assertEqual(hasil.owner, user)
        self.assertEqual(hasil.result, 'Sobat Ngetech abiez!')