from django.urls import path
from .views import *

app_name = 'tech_survey'

urlpatterns = [
    path('', show_tech_survey, name='show-tech-survey'),
    path('result-json/', get_result_json, name='result-json'),
    path('post-survey-for-flutter/', post_survey_result_for_flutter, name='post-survey-for-flutter'),
    path('get-survey-for-flutter/', get_current_result_for_flutter, name='get-survey-for-flutter'),
]