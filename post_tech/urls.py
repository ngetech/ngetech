from django.urls import path
from post_tech.views import *

app_name = 'post-tech'

urlpatterns = [
    path('', show_post_tech, name='show-post-tech'),
    path('add-post-tech/', add_post_tech, name='add-post-tech'),
    path('post-tech-json/', get_tech_post, name='get-tech-post'),
]
