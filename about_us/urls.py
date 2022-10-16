from django.urls import path
from about_us.views import *

app_name = 'about-us'

urlpatterns = [
    path('', about_us, name='about-us'),
]
