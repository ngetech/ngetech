from django.urls import path
from .views import *

app_name = 'tech_survey'

urlpatterns = [
    path('', show_tech_survey, name='show-tech-survey'),
    path('result-json/', get_result_json, name='result-json'),
]